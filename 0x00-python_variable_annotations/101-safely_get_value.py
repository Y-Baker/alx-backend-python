#!/usr/bin/env python3
"""Python typing annotations"""

from typing import TypeVar, Union, Any, Mapping, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[Union[T, None]] = None
                     ) -> Union[T, Any]:
    if key in dct:
        return dct[key]
    else:
        return default
