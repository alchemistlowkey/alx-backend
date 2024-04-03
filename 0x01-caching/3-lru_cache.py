#!/usr/bin/env python3
"""
Defines a LRUCache class that inherits from BaseCaching & is a caching system
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    Defines a caching system using LRU eviction
    """

    def __init__(self):
        """
        Initializes the LRUCache instance
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= self.MAX_ITEMS:
            throway, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {throway}")

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache
        """
        if key in self.cache_data:
            item = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = item
            return item
        return None
