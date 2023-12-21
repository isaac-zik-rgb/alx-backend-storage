#!/usr/bin/env python3
"""Create a store method that takes a data argument and returns a string.
The method should generate a random key (e.g. using uuid), store the input
data in Redis using the random key and return the key."""

import uuid
import redis
from typing import Union


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
