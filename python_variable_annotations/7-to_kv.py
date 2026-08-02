#!/usr/bin/env python3
"""
Module providing a type‑annotated function that returns a tuple containing a
string and the square of a numeric value. The second element of the tuple is
always a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is a string and the second element
    is the square of the provided number as a float.

    Args:
        k (str): The string key.
        v (Union[int, float]): The numeric value to square.

    Returns:
        Tuple[str, float]: A tuple containing k and the square of v.
    """
    return (k, float(v ** 2))
