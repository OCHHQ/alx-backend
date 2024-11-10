#!/usr/bin/python3
""" FIFO caching module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.order = []  # List to maintain the order of keys

    def put(self, key, item):
        """ Add an item in the cache using FIFO """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Remove the first item added (FIFO)
                    first_key = self.order.pop(0)
                    del self.cache_data[first_key]
                    print(f"DISCARD: {first_key}")

            self.cache_data[key] = item
            if key not in self.order:
                self.order.append(key)  # Keep track of the order

    def get(self, key):
        """ Retrieve an item from the cache """
        return self.cache_data.get(key, None)
