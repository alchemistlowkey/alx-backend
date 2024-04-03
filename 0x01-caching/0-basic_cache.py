#!/usr/bin/env python3
"""
Defines a BasicCache class that inherits from BaseCaching & is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a basic caching system
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
