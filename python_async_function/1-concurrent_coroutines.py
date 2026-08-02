#!/usr/bin/env python3
"""
Module providing an async routine that runs multiple coroutines concurrently.
This module contains a function that spawns wait_random several times and
returns the delays in ascending order based on completion time.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the given max_delay and return the list
    of delays in the order they complete.

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum delay for each wait_random call.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
