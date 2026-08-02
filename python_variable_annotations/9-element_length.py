#!/usr/bin/env python3
"""
Module providing a type‑annotated function that returns the length of each
element in an iterable sequence. Each element must support the len() function.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence-like elements.

    Returns:
        List[Tuple[Sequence, int]]: A list where each tuple contains an element
        from lst and the integer length of that element.
    """
    return [(i, len(i)) for i in lst]
