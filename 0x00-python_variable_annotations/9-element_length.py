#!/usr/bin/env python3
"This is a line of text"
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    "this is a line of text"
    return [(i, len(i)) for i in lst]
