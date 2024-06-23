#!/usr/bin/env python3
"""Reddis Database class
"""
from typing import Union
import redis
import uuid


class Cache():
    """
        The Redis data service class
    """
    def __init__(self) -> None:
        """Create the redis server connection"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key and store data using the generated key"""
        if not data:
            return ""

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
