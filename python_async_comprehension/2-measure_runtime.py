#!/usr/bin/env python3
"""
Module providing a coroutine that measures the runtime of executing
async_comprehension four times in parallel using asyncio.gather.
"""

import asyncio
import time
from typing import float
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel and measure
    the total runtime.

    Returns:
        float: Total runtime in seconds.
    """
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time.time()
    return end - start
