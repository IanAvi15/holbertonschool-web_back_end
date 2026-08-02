#!/usr/bin/env python3
"""
Module providing a type‑annotated function that sums a list of floats.
This module contains a function that returns the total of all floating‑point
numbers in a given list.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of a list of floating‑point numbers.

    Args:
        input_list (List[float]): The list of floats to sum.

    Returns:
        float: The total value of all elements in input_list.
    """
    return sum(input_list)
