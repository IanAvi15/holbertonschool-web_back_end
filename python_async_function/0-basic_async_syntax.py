#!/usr/bin/env python3
"""
Module providing an asynchronous coroutine that waits for a random delay
and returns that delay as a float.
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay allowed.

    Returns:
        float: The randomly generated delay.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
