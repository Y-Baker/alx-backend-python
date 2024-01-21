#!/usr/bin/env python3
"""Type Checking"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """type-annotated function safe_first_element that takes a list input_list"""
    if lst:
        return lst[0]
    else:
        return None
