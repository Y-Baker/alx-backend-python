#!/usr/bin/env python3
"""Aysnc Generator Function"""

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """will loop 10 times, each time asynchronously wait 1 second"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
