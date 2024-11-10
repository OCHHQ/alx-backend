#!/usr/bin/python3
""" LRU Caching Module """

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRU Caching System """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache using LRU strategy """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If the key already exists, remove it to update its position
            self.cache_data.pop(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the least recently used item
            lru_key = next(iter(self.cache_data))
            print(f"DISCARD: {lru_key}")
            self.cache_data.pop(lru_key)

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        # Move the accessed item to the end to mark it as recently used
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
