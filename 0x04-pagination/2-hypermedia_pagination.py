#!/usr/bin/env python3
"This is a line of text"
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int]:
    "This is a line of text"
    return page * page_size - page_size, page * page_size


class Server:
    "This is a line of text"
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        "This is a line of text"
        self.__dataset = None

    def dataset(self) -> List[List]:
        "This is a line of text"
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        "This is a line of text"
        assert type(page) == int and type(page_size) == int
        assert page > 0 or page_size > 0
        dataset = self.dataset()
        start, last = index_range(page, page_size)
        return dataset[start:last]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        "This is a line of text"
        total_pages = math.ceil(len(self.dataset()) / page_size)
        if page < total_pages:
            page_size = page_size
        else:
            page_size = 0
        data = self.get_page(page, page_size)
        next_page = None
        if page < total_pages:
            next_page = page + 1
        prev_page = None
        if page > 1:
            prev_page = page - 1
        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }
