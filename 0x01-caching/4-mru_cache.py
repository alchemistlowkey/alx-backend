#!/usr/bin/env python3
"""
Defines a MRUCache class that inherits from BaseCaching & is a caching system
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Defines a caching system using MRU eviction
    """

    def __init__(self):
        """
        Initializes the MRUCache instance
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = list(self.cache_data.keys())[-1]
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache
        """
        if key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None
