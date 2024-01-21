#!/usr/bin/env python3
"""module for task 8"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    functionn that takes a float multiplier as argument and returns a function
    """
    def return_func(n: float) -> float:
        """function that multiplies a float by multiplier"""
        return n * multiplier

    return return_func
