#!/usr/bin/env python3
"""Module for measure_time func"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure time needed for wait_n func to complete"""
    start: float = time.monotonic()
    asyncio.run(wait_n(n, max_delay))

    return (time.monotonic() - start) / n
