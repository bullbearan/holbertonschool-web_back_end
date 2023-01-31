#!/usr/bin/env python3
"This is a line of text"
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    "This is a line of text"
    return page * page_size - page_size, page * page_size
