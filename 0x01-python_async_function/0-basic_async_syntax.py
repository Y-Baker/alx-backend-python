#!/usr/bin/env python3
"""Aync basics in Python task 0"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Aync basics in Python task 0"""

    random_value = random.uniform(0, max_delay)
    await asyncio.sleep(random_value)

    return random_value
