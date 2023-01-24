#!/usr/bin/env python3
"This is a line of text"
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    "this is a line of text"
    n = random.uniform(0, max_delay)
    await asyncio.sleep(n)
    return n
