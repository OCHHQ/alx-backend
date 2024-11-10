#!/usr/bin/python3
"""FIFO Caaching system"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class that inherit from BaseCaching
    implement a FIFO caching system"""

    def __init__(self):
        """initializing the cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add a item  to the cache using FIFO policy"""
        if key is None or item is None:
            return
        if (key not in self.cache_data and
           len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            # in python pop mean delete 0 first key
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"Discard: {first_key}")

        # i would had key and item to the cache
        self.cache_data[key] = item
        if key not in self.order:
            self.order.append(key)  # keep track of order key

    def get(self, key):
        """Get an item from the cache"""
        return self.cache_data.get(key, None)
