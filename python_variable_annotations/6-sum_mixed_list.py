#!/usr/bin/env python3
"""
Module providing a type‑annotated function that sums a mixed list of integers
and floating‑point numbers. This module contains a function that returns the
total of all numeric values in the provided list.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of numbers to sum.

    Returns:
        float: The total value of all elements in mxd_lst.
    """
    return sum(mxd_lst)
