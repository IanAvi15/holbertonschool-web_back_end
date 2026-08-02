#!/usr/bin/env python3
"""
Module providing a type‑annotated function that creates multiplier functions.
This module contains a higher‑order function that returns another function
capable of multiplying a float by a predefined multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The value used to multiply future inputs.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product as a float.
    """
    def multiply(value: float) -> float:
        return value * multiplier

    return multiply
