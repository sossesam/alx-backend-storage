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


def call_history(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        base_key = method.__qualname__
        input_key = f"{base_key}:inputs"
        output_key = f"{base_key}:outputs"
        input_data = str(args)
        self._redis.rpush(input_key, input_data)
        output = method(self, *args, **kwargs)
        output_data = str(output)
        self._redis.rpush(output_key, output_data)
        return output
    return wrapper


def replay(method):

    cache = method.__self__
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"
    inputs = cache._redis.lrange(input_key, 0, -1)
    outputs = cache._redis.lrange(output_key, 0, -1)
    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for input, output in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{input.decode('utf-8')}) ->
              {output.decode('utf-8')}")


class Cache:
    def __init__(self):
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()

    @call_history
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
