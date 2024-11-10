from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
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
        if key is None or key not in self.cache_data:
            return None

        # Mark the key as most recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
