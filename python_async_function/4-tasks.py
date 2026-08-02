#!/usr/bin/env python3
"""
Module providing an async routine that runs multiple asyncio.Tasks created
from task_wait_random. The delays are returned in the order tasks complete.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the given max_delay and return the
    list of delays in the order they complete.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of delays in ascending order based on completion.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
