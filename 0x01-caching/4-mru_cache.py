#!/usr/bin/python3
"""
MRU Caching Module
This module implements a Most Recently Used (MRU)
caching system using OrderedDict.
The MRU caching system removes the most recently
used item when the cache is full.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    MRU (Most Recently Used) caching system
    This class implements a caching system using the MRU algorithm.
    When the cache is full, it removes the most recently used item.
    Attributes:
    cache_data (OrderedDict): Ordered dictionary to store cache items
    """
    def __init__(self):
        """Initialize the MRU cache using OrderedDict"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache using MRU algorithm
        Args:
            key: The key to identify the item
            item: The value to be stored
        If the cache is full, removes the most recently used item
        before adding the new item.
        """
        if key is None or item is None:
            return

        # If the key is already in the cache, update it and move to end
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the most recently used item (last one in OrderedDict)
            last_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {last_key}")

        # Add or update the item in the cache and mark as most recently used
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache

        Args:
            key: The key to identify the item

        Returns:
            The value linked to the key if it exists, None otherwise
        """
        if key is None or key not in self.cache_data:
            return None

        # Mark the key as most recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
