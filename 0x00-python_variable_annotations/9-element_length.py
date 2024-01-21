#!/usr/bin/env python3
"""Type Checking"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that takes a list lst of strings and returns a list of tuples
    """

    return [(i, len(i)) for i in lst]
