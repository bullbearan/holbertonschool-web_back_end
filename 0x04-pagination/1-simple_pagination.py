#!/usr/bin/env python3
"This is a line of text"
from typing import Tuple, List
import csv


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
        assert page > 0 and page_size > 0
        dataset = self.dataset()
        start, last = index_range(page, page_size)
        return dataset[start:last]
