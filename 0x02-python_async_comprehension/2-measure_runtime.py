#!/usr/bin/env python3
"This is a line of text"
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    "this is a line of text"
    a = time.time()
    await asyncio.gather(async_comprehension())
    b = time.time()
    return b - a
