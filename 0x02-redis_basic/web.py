#!/usr/bin/env python3
import requests
import redis
import functools

r = redis.Redis()

def count_url_request(fn):
    """A decorator to count the number of requests to a URL"""

    @functools.wraps(fn)
    def wrapper(url: str):
        """A wrapper function"""
        key = key = f"count:{url}"
        cache_key = f"cache:{url}"
        cached_result = r.get(cache_key)
        if cached_result:
            return cached_result

        r.incr(key)
        res =  fn(url)
        r.set(cache_key, res, 10)
        return res
    return wrapper


def get_page(url: str) -> str:
    """Obtain the HTML content of a particular URL and return it."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.text

if __name__ == '__main__':
    url = "http://slowwly.robertomurray.co.uk"
    content = get_page(url)
    print(content)
