#!/usr/bin/env python3
"This is a line of text"
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    "this is a line of text"
    if lst:
        return lst[0]
    else:
        return None
