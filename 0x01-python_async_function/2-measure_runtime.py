#!/usr/bin/env python3
"This is a line of text"
from asyncio import run
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    "this is a line of text"
    a = time.time()
    run(wait_n(n, max_delay))
    b = time.time()
    return (b - a) / n
