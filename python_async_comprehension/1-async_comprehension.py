#!/usr/bin/env python3
"""
Module providing a coroutine that collects values from an async generator
using an async comprehension.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers from async_generator using an async
    comprehension and return them as a list.

    Returns:
        List[float]: A list containing 10 random float values.
    """
    return [value async for value in async_generator()]
