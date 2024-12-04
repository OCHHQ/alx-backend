#!/usr/bin/python3
"""
LFU Caching Module
This module implements a Least Frequently Used
(LFU) caching system with LRU as tiebreaker
"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    LFU (Least Frequently Used) caching system
    Uses LRU as a tiebreaker when multiple items have the same access frequency

    Attributes:
        cache_data (dict): Dictionary to store cache items
        freq (defaultdict): Dictionary to store frequencies of items
        freq_items (defaultdict): Dictionary to store items of each frequency
        min_freq (int): Current minimum frequency
    """

    def __init__(self):
        """Initialize the LFU cache"""
        super().__init__()
        self.freq = {}  # key -> frequency
        # frequency -> OrderedDict of keys
        self.freq_items = defaultdict(OrderedDict)
        self.min_freq = 0

    def _update_freq(self, key):
        """
        Update frequency of an item and related data structures

        Args:
            key: The key whose frequency needs to be updated
        """
        # Get current frequency of key
        curr_freq = self.freq.get(key, 0)
        # Increase frequency
        self.freq[key] = curr_freq + 1
        # If key exists in current frequency, remove it
        if curr_freq > 0:
            del self.freq_items[curr_freq][key]
            # If current frequency bucket is empty and it's the min frequency
            if not self.freq_items[curr_freq] and curr_freq == self.min_freq:
                self.min_freq += 1
        else:
            # For new items
            self.min_freq = 1

        # Add key to new frequency bucket
        self.freq_items[curr_freq + 1][key] = key

    def put(self, key, item):
        """
        Add an item to the cache using LFU algorithm with LRU as tiebreaker
        Args:
            key: The key to identify the item
            item: The value to be stored

        If cache is full, removes the least frequently used item.
        If there's a tie, removes the least recently used among
        the least frequently used items.
        """
        if key is None or item is None:
            return

        # If key exists, update frequency and value
        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_freq(key)
            return

        # If cache is full, remove LFU item
        if len(self.cache_data) >= self.MAX_ITEMS:
            # Get least frequently used items
            lfu_items = self.freq_items[self.min_freq]
            # Get least recently used among them (first item in OrderedDict)
            lfu_key, _ = lfu_items.popitem(last=False)
            del self.cache_data[lfu_key]
            del self.freq[lfu_key]
            print(f"DISCARD: {lfu_key}")

        # Add new item
        self.cache_data[key] = item
        self._update_freq(key)

    def get(self, key):
        """
        Retrieve an item from the cache

        Args:
            key: The key to identify the item

        Returns:
            The value linked to the key if it exists, None otherwise

        Updates item frequency on successful retrieval
        """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency of accessed item
        self._update_freq(key)
        return self.cache_data[key]
