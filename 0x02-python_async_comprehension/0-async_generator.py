#!/usr/bin/env python3
"This is a line of text"
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    "this is a line of text"
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
