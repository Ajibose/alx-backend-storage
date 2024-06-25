#!/usr/bin/env python3
"""Write a fucntion that obtain the HTML content of a URL using request mod"""
import requests
import functools
import redis


def count_request(fn):
    """A decorator function to cache the number of request to a url"""
    r = redis.Redis()

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        """A wrapper function"""
        key_count = r.get(f"count:{args[0]}")
        key = f"count:{args[0]}"
        if not key_count:
            r.set(key, 0, 10)

        res = fn(*args, **kwargs)
        if res:
            r.incr(key)
        return res

    return wrapper

@count_request
def get_page(url: str) -> str:
    """obtain the HTML content of a particular URL and returns it."""
    response = requests.get(url)

    content = ""
    if response.status_code == 200:
        content = response.text
     
    return content

if __name__ == '__main__':
    content = get_page("http://slowwly.robertomurray.co.uk")
    print(content)
