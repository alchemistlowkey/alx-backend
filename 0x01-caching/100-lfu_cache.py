#!/usr/bin/env python3
"""
Defines a LFUCache class that inherits from BaseCaching & is a caching system
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """
    Defines a caching system using LFU eviction
    """

    def __init__(self):
        """
        Initializes the LFUCache instance
        """
        super().__init__()
        self.cache_dict = defaultdict(int)

    def put(self, key, item):
        """
        Add an item to the cache
        """

        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data[key] = item
                    self.cache_dict[key] += 1
                    return
                min_freq = min(self.cache_dict.values())
                lfu_item = [k for k, v in self.cache_dict.items()
                            if v == min_freq]

                if len(lfu_item) > 1:
                    item_discarded = lfu_item[0]
                else:
                    item_discarded = lfu_item[0]
                del self.cache_data[item_discarded]
                print(f"DISCARD: {item_discarded}")
                del self.cache_dict[item_discarded]

            self.cache_data[key] = item
            self.cache_dict[key] += 1

    def get(self, key):
        """
        Retrieve an item from the cache
        """
        if key in self.cache_data:
            self.cache_dict[key] += 1
            return self.cache_data[key]
        return None
