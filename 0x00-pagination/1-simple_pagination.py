#!/usr/bin/env python3
"""
Implement a method named get_page that takes two integer arguments page
with default value 1 and page_size with default value 10.
You have to use this CSV file 'Popular_Baby_Names.csv' from the readme
Use assert to verify that both arguments are integers greater than 0.
Use index_range to find the correct indexes to paginate the dataset correctly
and return the appropriate page of the dataset (i.e. the correct list of rows)
If the input arguments are out of range for the dataset,
an empty list should be returned.
"""
import csv
import math
from typing import List


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


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of the dataset.

        Args:
            page: The page number (1-indexed). Default is 1.
            page_size: The number of items per page. Default is 10.

        Returns:
            A list of rows corresponding to the requested page.
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        items = len(dataset)
        total_pages = math.ceil(items / page_size)

        if page > total_pages:
            return []

        start_index, end_index = index_range(page, page_size)
        return dataset[start_index:end_index]
