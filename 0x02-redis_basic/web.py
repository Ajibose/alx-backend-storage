#!/usr/bin/env python3
"""In this tasks, we will implement a get_page function
(prototype: def get_page(url: str) -> str:). The core of
the function is very simple. It uses the requests module
to obtain the HTML content of a particular URL and returns it.

Start in a new file named web.py and do not reuse the code
written in exercise.py.

Inside get_page track how many times a particular URL was
accessed in the key "count:{url}" and cache the result with
an expiration time of 10 seconds.

Tip: Use http://slowwly.robertomurray.co.uk to simulate
a slow response and test your caching.
"""
import requests
import redis
import functools


r = redis.Redis()


def count_url_request(fn):
    """A decorator to count the number of requests to a URL"""
    r = redis.Redis()

    def wrapper(url: str):
        """A wrapper function"""
        key = f"count:{url}"
        cache_key = f"cache:{url}"
        cached_result = r.get(cache_key)
        if cached_result:
            r.incr(key)
            return cached_result.decode("utf-8")

        r.incr(key)
        res = fn(url)
        r.set(cache_key, res, 10)
        return res
    return wrapper


@count_url_request
def get_page(url: str) -> str:
    """Obtain the HTML content of a particular URL and return it."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.text


if __name__ == '__main__':
    url = "http://slowwly.robertomurray.co.uk"
    content = get_page(url)
    print(content)
