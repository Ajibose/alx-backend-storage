#!/usr/bin/env python3
"""Reddis Database class
"""
from typing import Union, Callable, Optional
import redis
import uuid
import functools


def count_calls(method: Callable) -> Callable:
    """Count how many times fn was called"""
    key = method.__qualname__

    @functools.wraps(method)
    def warpper(self, *args, **kwargs):
        """Wraps around a method"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return warpper


class Cache():
    """
        The Redis data service class
    """
    def __init__(self) -> None:
        """Create the redis server connection"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key and store data using the generated key"""
        if not data:
            return ""

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[
            Callable] = None) -> Union[str, bytes, int, float]:
        """Retrieve data from the server and trnsaform"""
        val = self._redis.get(key)
        if val and fn:
            val = fn(val)

        return val

    def get_int(self, key: str) -> int:
        """Retrieve data from the server and trnsaform integer"""
        return self.get(key, int)

    def get_str(self, key: str) -> str:
        """Retrieve data from the server and trnsaform to string"""
        val = self.get(key, lambda d: d.decode('utf-8'))
        return val
