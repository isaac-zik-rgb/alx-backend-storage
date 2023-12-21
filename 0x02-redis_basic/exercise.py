#!/usr/bin/env python3
"""Create a store method that takes a data argument and returns a string.
The method should generate a random key (e.g. using uuid), store the input
data in Redis using the random key and return the key."""

import uuid
import redis
from typing import Union, Optional, Callable


class Cache:
    """Cache class.that def __init__ method, store an instance of the
Redis client as a private variable"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) ->
    Union[str, int, bytes, None]:
        '''convert the data back to the desired format'''

        retrive_data = self._redis.get(key)

        if retrive_data is None:
            return None
        return fn(retrive_data)

    def get_str(self, key: str) -> str:
        '''parametrize Cache.get with correct conversion function'''
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> Union[int, None]:
        '''parametrize Cache.get with correct conversion function'''
        value = self._get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
