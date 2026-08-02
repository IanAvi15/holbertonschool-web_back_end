#!/usr/bin/env python3
"""
Module providing a type‑annotated function for computing the floor of a float.
This module contains a function that returns the largest integer less than or
equal to a given floating‑point number.
"""

import math


def floor(n: float) -> int:
    """
    Return the floor value of a floating‑point number.

    Args:
        n (float): The number to floor.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
