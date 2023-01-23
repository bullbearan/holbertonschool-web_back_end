#!/usr/bin/env python3
"This is a line of text"
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    "this is a line of text"
    res = 0
    for i in mxd_lst:
        res += i
    return res
