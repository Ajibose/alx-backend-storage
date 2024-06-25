#!/usr/bin/env python3
"""Reddis Database class
"""
from typing import Union, Callable, Optional
import redis
import uuid
import functools


def replay(method: Callable):
    """display the history of calls of a particular function"""
    method_name = method.__qualname__
    instance = method.__self__
    cls_name = type(instance).__name__

    #redis = getattr(instance, "_redis", None)
    if not redis:
        print("Redis connection not found")
        return

    r = redis.Redis()

    method_called_times = r.get(method_name)
    input_list = r.lrange(f"{method_name}:inputs", 0, -1)
    output_list = r.lrange(f"{method_name}:outputs", 0, -1)
    print(list(output_list))
    print(f"{method_name} was called {int(method_called_times)} times:")
    for (input_data, output_data) in zip(input_list, output_list):
        try:
            input_data = input_data.decode('utf-8')
        except Exception:
            input_data = ""

        try:
            output_data = output_data.decode('utf-8')
        except Exception:
            output_data = ""
        print(f"{method_name}(*{input_data}) -> {output_data}")


def call_history(method: Callable) -> Callable:
    """Decorated function to tore the input from and output to the server"""
    method_name = method.__qualname__
    input_key = f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """The wrapper for storing history"""
        self._redis.rpush(input_key, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(output_key, res)
        return res

    return wrapper


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

    @call_history
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
