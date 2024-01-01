#!/usr/bin/env python3
"""Module defines a class Server that mocks an API endpoint"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Mock of an API endpoint that returns a page based on
        page number and page size parameters
        """
        index_range = __import__('0-simple_helper_function').index_range

        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        try:
            result = self.dataset()[start: end]
        except IndexError:
            result = []
        finally:
            return result

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Similar to get_page() above
        but returns hypermedia(references to some info?)
        """
        data = {'page_size': 0, 'page': 0, 'data': [], 'next_page': 0,
                'prev_page': 0, 'total_pages': 0}
        page_data = self.get_page(page, page_size)
        data['page_size'] = len(page_data)
        data['page'] = page
        data['data'] = page_data
        data['prev_page'] = page - 1 if page >= 2 else None
        if page_size * page < len(self.dataset()):
            data['next_page'] = page + 1
        else:
            data['next_page'] = None
        data['total_pages'] = math.ceil(len(self.dataset()) / page_size)
        return data
