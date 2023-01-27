#!/usr/bin/env python3
"This is a line of text"
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    "This is a line of text"
    def __init__(self):
        "This is a line of text"
        super().__init__()
        self.last = ''

    def put(self, key, item):
        "This is a line of text"
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD:", self.last)
                del self.cache_data[self.last]
            self.last = key

    def get(self, key):
        "This is a line of text"
        return self.cache_data.get(key)
