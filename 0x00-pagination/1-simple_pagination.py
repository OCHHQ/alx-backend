#!/usr/bin/env python3
"""
Simple pagination using a Server class to paginate a dataset.
"""

import csv
from typing import List, Tuple


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
        # Validate input arguments
        assert all(
            isinstance(arg, int) and arg > 0 for arg in [page, page_size]
        ), "Both page and page_size must be positive integers"

        # Calculate start and end indexes
        start_index, end_index = index_range(page, page_size)

        # Get the dataset
        data = self.dataset()

        # Return appropr page of the dataset or an empty list if out of rang
        if start_index >= len(data):
            return []

        return data[start_index:end_index]
