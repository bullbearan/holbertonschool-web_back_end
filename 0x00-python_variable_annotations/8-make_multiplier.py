#!/usr/bin/env python3
"This is a line of text"
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    "this is a line of text"
    def _float(n: float) -> float:
        "this is a line of text"
        return float(n * multiplier)
    return _float
