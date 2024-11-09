#!/usr/bin/env python3
"""
Hypermedia pagination using a Server class to paginate a dataset.
here i am student every line of code comment aim
to help me retain and recall
"""

import csv
from typing import List, Tuple, Dict, Any
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset based on the page and page_size."""
        assert all(
            isinstance(arg, int) and arg > 0 for arg in [page, page_size]
        ), "Both page and page_size must be positive integers"

        # Calculate start and end indexes
        start_index, end_index = index_range(page, page_size)

        # Get the dataset
        data = self.dataset()

        # Re the approiate page of the dataset or an empty list if out of range
        if start_index >= len(data):
            return []

        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return a dictionary with hypermedia pagination information."""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        # Calculate next_page and prev_page
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
