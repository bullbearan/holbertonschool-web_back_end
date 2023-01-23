#!/usr/bin/env python3
"This is a line of text"
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    "this is a line of text"
    res = (k, v**2)
    return res
