#!/usr/bin/env python3
"This is a line of text"
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    "This is a line of text"
    def __init__(self):
        "This is a line of text"
        super().__init__()

    def put(self, key, item):
        "This is a line of text"
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                ele = list(self.cache_data.keys())[0]
                print("DISCARD:", ele)
                del self.cache_data[ele]

    def get(self, key):
        "This is a line of text"
        return self.cache_data.get(key)
