#!/usr/bin/python3
""" MRU Caching Module """

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRU Caching System """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache using MRU strategy """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If the key already exists, remove it to update its position
            self.cache_data.pop(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the most recently used item
            mru_key = next(reversed(self.cache_data))
            print(f"DISCARD: {mru_key}")
            self.cache_data.pop(mru_key)

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        # Move the accessed item to the end to mark it as most recently used
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
