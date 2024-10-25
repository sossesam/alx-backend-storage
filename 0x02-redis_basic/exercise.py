#!/usr/bin/env python3
"""0x02. Redis basic"""
import redis
import uuid


class Cache:
    """0x02. Redis basic"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        id = str(uuid.uuid4())
        self._redis.mset({id:data})
        return id