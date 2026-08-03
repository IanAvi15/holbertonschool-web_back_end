#!/usr/bin/env python3
"""
Module providing an asynchronous generator that yields random numbers.
This generator waits 1 second between yields and produces 10 values.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously yield 10 random numbers between 0 and 10.

    Each iteration waits 1 second before yielding the next value.

    Returns:
        AsyncGenerator[float, None]: An async generator producing floats.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
