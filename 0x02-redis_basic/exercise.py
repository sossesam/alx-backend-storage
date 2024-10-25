#!/usr/bin/env python3
import redis
import uuid

class Cache:
    def __init__(self):
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()

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
