#!/usr/bin/env python3
"""
Implement a get_hyper method that takes the same arguments (and defaults) as
get_page and returns a dictionary containing the following key-value pairs:
page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.
You can use the math module if necessary.
"""
import csv
import math
from typing import List, Dict, Union


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

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str,
                                               Union[int, List[List], None]]:
        """
        Retrieve hypermedia information for a specific page.

        Args:
            page: The page number (1-indexed). Default is 1.
            page_size: The number of items per page. Default is 10.

        Returns:
            A dict containing hypermedia information for the requested page.
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset_page = self.get_page(page, page_size)
        items = len(self.dataset())
        total_pages = math.ceil(items / page_size)

        hyper_info = {
            "page_size": len(dataset_page),
            "page": page,
            "data": dataset_page,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

        return hyper_info
