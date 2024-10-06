#!/usr/bin/env python3
"""A module with 1 Class: Cache"""
import redis
import uuid
from typing import Union, Optional, Callable


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

    def get_str(self, data: bytes) -> str:
        ''' automatically parametrize Cache.get
            with str conversion function.
        '''
        return str(data)

    def get_int(self, data: bytes) -> int:
        ''' automatically parametrize Cache.get
            with the int conversion function.
        '''
        return int(data)

    def get(self,
            key: str,
            fn: Optional[Callable]
            ) -> Union[str, bytes, int, float]:
        '''Convert data to desired format'''
        value = self._redis.get(key)
        if isinstance(fn, int):
            return self.get_int(value)
        if isinstance(fn, str):
            return self.get_str(value)
        if fn is None:
            return value
        return fn(value)
