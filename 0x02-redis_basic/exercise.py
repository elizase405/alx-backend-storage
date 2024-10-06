#!/usr/bin/env python3
"""A module with 1 Class: Cache"""
import redis
import uuid
from typing import Union


class Cache:
    """Create Cache class"""

    def __init__(self):
        '''initialize'''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''store data in redis
            Args:
                data - data to be stored in redis
            Return:
                The data stored in redis
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
