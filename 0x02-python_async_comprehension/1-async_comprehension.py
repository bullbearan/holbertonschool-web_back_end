#!/usr/bin/env python3
"This is a line of text"
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    "this is a line of text"
    lst = []
    async for i in async_generator():
        lst.append(i)
    return lst
