#!/usr/bin/env python3
import requests
import redis
import functools

# Initialize Redis client
r = redis.Redis()

def count_request(fn):
    """A decorator to count the number of requests to a URL"""
    @functools.wraps(fn)
    def wrapper(url: str):
        """A wrapper function"""
        key = f"count:{url}"
        r.incr(key)
        return fn(url)
    return wrapper

def cache_result(expire_time: int):
    """A decorator to cache the result of a function with expiration"""
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(url: str):
            """A wrapper function"""
            cache_key = f"cache:{url}"
            cached_result = r.get(cache_key)
            if cached_result:
                return cached_result.decode('utf-8')
            result = fn(url)
            r.setex(cache_key, expire_time, result)
            return result
        return wrapper
    return decorator

@count_request
@cache_result(10)
def get_page(url: str) -> str:
    """Obtain the HTML content of a particular URL and return it."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.text

if __name__ == '__main__':
    url = "http://slowwly.robertomurray.co.uk"
    content = get_page(url)
    print(content)
