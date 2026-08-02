#!/usr/bin/env python3
"""
Module providing a function that measures the average runtime of executing
wait_n. This module uses the time module to compute approximate elapsed time.
"""

import asyncio
import time
from typing import Union
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time of wait_n(n, max_delay) and return
    the average time per coroutine.

    Args:
        n (int): Number of coroutines to execute.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average execution time per coroutine.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start
    return total_time / n
