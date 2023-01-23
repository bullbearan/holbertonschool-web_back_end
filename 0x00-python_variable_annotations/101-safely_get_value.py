#!/usr/bin/env python3
"This is a line of text"
from typing import Union, Any, Mapping, TypeVar


t = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[t, None] = None) -> Union[Any, t]:
    "this is a line of text"
    if key in dct:
        return dct[key]
    else:
        return default
