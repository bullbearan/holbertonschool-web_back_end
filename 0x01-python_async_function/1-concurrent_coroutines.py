#!/usr/bin/env python3
"This is a line of text"
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    "this is a line of text"
    lst = []
    for i in range(n):
        lst.append(await wait_random(max_delay))
    return sorted(lst)
