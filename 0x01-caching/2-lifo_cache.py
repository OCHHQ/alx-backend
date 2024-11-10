#!/usr/bin/python3
""" LIFO Caching Module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching system """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item to the cache using LIFO strategy """
        if key is None or item is None:
            return

        # Add the item to the cache
        self.cache_data[key] = item

        # Check if the cache exceeds the maximum allowed items
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key is not None:
                print(f"DISCARD: {self.last_key}")
                del self.cache_data[self.last_key]

        # Update the last key
        self.last_key = key

    def get(self, key):
        """ Retrieve an item from the cache """
        return self.cache_data.get(key, None)
