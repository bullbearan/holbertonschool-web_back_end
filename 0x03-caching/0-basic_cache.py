#!/usr/bin/env python3
"This is a line of text"
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    "This is a line of text"
    def put(self, key, item):
        "This is a line of text"
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        "This is a line of text"
        return self.cache_data.get(key)
