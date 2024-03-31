#!/usr/bin/env python3
"""
A function named index_range that takes two integer arguments page & page_size
The function should return a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return in a list
for those particular pagination parameters.
Page numbers are 1-indexed, i.e. the first page is page 1.
"""


def index_range(page, page_size):
    """
    Calculate the start and end index for a given page and page size.

    Args:
        page: The page number (1-indexed).
        page_size: The number of items per page.

    Returns:
        A tuple containing the start index and end index for the given page.
    """

    start_index = (page - 1) * page_size
    end_index = page_size + start_index

    return start_index, end_index
