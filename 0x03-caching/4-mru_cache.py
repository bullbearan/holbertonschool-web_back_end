#!/usr/bin/env python3
"This is a line of text"
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    "This is a line of text"
    def __init__(self):
        "This is a line of text"
        super().__init__()
        self.least = []

    def put(self, key, item):
        "This is a line of text"
        if key and item:
            if self.cache_data.get(key):
                self.least.remove(key)
            while len(self.least) >= self.MAX_ITEMS:
                rm = self.least.pop()
                self.cache_data.pop(rm)
                print("DISCARD:", rm)
            self.least.append(key)
            self.cache_data[key] = item

    def get(self, key):
        "This is a line of text"
        if self.cache_data.get(key):
            self.least.remove(key)
            self.least.append(key)
        return self.cache_data.get(key)
