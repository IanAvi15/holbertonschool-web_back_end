#!/usr/bin/env python3
"""
Module providing a regular function that returns an asyncio.Task wrapping
the wait_random coroutine.
"""

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Return an asyncio.Task that executes wait_random with the given max_delay.

    Args:
        max_delay (int): Maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: A task wrapping the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
