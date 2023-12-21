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
    Union[str, int, None]:
        retrive_data = self._redis.get(key)

        if retrive_data is None:
            return None
        return fn(retrive_data) if (fn and callable(fn)) else retrive_data

    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, fn=lambda data: data.decode("utf-8")
                        if isinstance(data, byte) else data)

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, fn=lambda data: int(data)
                        if isinstance(data, byte) else data)
