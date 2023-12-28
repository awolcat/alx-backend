#!/usr/bin/env python3
"""Module defines a pagination helper function"""
from typing import *


def index_range(page:int, page_size:int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return
    in a list for those particular pagination parameters.
    """
    if page <= 1:
        return (page, page_size)
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
