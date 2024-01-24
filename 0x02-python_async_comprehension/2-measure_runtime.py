#!/usr/bin/env python3
"""Task 2"""

from time import monotonic
from asyncio import gather
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime of execute async_comprehension
    four times in parallel using asyncio.gather"""

    start = monotonic()
    await gather(*[async_comprehension() for _ in range(4)])

    return monotonic() - start
