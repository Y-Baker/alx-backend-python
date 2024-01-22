#!/usr/bin/env python3
"""module for task_wait_n func"""

import asyncio
from typing import List
from time import monotonic
wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n func that spawn wait_random n times with the specified max_delay
    """
    re: List[float] = []
    for i in range(n):
        start = monotonic()
        await wait_random(max_delay)
        re.append(monotonic() - start)

    return sorted(re)
