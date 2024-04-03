#!/usr/bin/env python3
"""
Defines a LIFOCache class that inherits from BaseCaching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Defines a caching system using LIFO eviction
    """

    def __init__(self):
        """
        Initializes the LIFOCache instance
        """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        Add an item to the cache
        """
        
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= self.MAX_ITEMS:
                last_item = self.cache_order.pop()
                del self.cache_data[last_item]
                print(f"DISCARD: {last_item}")

            self.cache_data[key] = item
            self.cache_order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
