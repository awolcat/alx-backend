#!/usr/bin/env python3
"""BasicCache module"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A Basic Cache"""

    def __init__(self):
        """Intitalize super and self"""
        super().__init__()

    def put(self, key, item):
        """Add item to cache with key key"""
        if key is None or item is None:
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """Return the value in cache linked to key"""
        if key is None:
            return None
        return self.cache_data.get(key)
