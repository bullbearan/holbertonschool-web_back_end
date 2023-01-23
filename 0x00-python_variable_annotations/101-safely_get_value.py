#!/usr/bin/env python3
"This is a line of text"
from typing import Union, Any, Mapping, TypeVar


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar('T'), None] = None) -> Union[Any, TypeVar('T')]:
    "this is a line of text"
    if key in dct:
        return dct[key]
    else:
        return default
