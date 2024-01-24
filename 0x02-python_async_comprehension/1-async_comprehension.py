#!/usr/bin/env python3
"""Task 1"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List:
    """
    collect 10 random nums using an async comprehensing over async_generator
    """
    return [_ async for _ in async_generator()]
