#!/usr/bin/env python3
""" BasicCache module for a simple caching system
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching
    It implements a caching system with no size limit.
    """

    def put(self, key, item):
        """ Add an item to the cache
        If key or item is None, do nothing
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache by its key
        If key is None or does not exist, return None
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
