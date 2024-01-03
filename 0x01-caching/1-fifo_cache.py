#!/usr/bin/env python3
"""BasicCache module"""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A FIFO Cache"""

    def __init__(self):
        """Intitalize super and self"""
        super().__init__()
        self.keyMeta = {}

    def put(self, key, item):
        """Add item to cache with key key"""
        if key is None or item is None:
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            # Delete oldest key, value pair
            cache_keys = list(self.cache_data.keys())
            time = datetime.now()
            for kc in cache_keys:
                if self.keyMeta[kc] < time:
                    time = self.keyMeta[kc]
                    first_in_key = kc
            # first_in_key = self.newKeys[0]
            if key not in cache_keys:
                self.cache_data.pop(first_in_key)
                print(f"DICARD {first_in_key}")
        self.cache_data.update({key: item})
        self.keyMeta.update({key: datetime.now()})

    def get(self, key):
        """Return the value in cache linked to key"""
        if key is None:
            return None
        return self.cache_data.get(key)
