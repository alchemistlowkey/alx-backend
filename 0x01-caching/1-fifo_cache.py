#!/usr/bin/env python3
"""
Defines a FIFOCache class that inherits from BaseCaching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Defines a caching system using FIFO eviction
    """

    def __init__(self):
        """
        Initializes the FIFOCache instance
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

        if len(self.cache_data) >= self.MAX_ITEMS:
            first_item = self.queue.pop(0)
            del self.cache_data[first_item]
            print(f"DISCARD: {first_item}")

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
