#!/usr/bin/env python3
"This is a line of text"
import redis
import requests


_redis = redis.Redis()
count = 0


def get_page(url: str) -> str:
    "This is a line of text"
    _redis.set(f"cached:{url}", count)
    res = requests.get(url)
    _redis.incr(f"count:{url}")
    _redis.setex(f"cached:{url}", 10, _redis.get(f"cached:{url}"))
    return res.text


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")
