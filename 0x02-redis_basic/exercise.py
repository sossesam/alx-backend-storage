#!/usr/bin/env python3
import redis
import uuid
from functools import wraps

def count_calls(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    def __init__(self):
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()
    @count_calls
    def store(self, data):
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        
        return id
    
    def get(self, key, fn=None):
        data = self._redis.get(key)

        if data is None:
            return data
        
        if fn:
            new_data = fn(data)
            return new_data
        else:
            return data
        
    def get_str(self, key):
        return self.get(key, lambda d: d.decode('utf-8'))
    
    def get_int(self, key):
        return self.get(key, lambda d: int(d))
