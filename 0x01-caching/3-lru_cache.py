#!/usr/bin/env python3
"""Create a class LRUCache that inherits from
BaseCaching and is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Least Recently Used
    """

    def __init__(self):
        """Least Recently Used
        """
        super().__init__()
        self.gotKeys = []

    def put(self, key, item):
        """Least Recently Used
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.gotKeys:
                self.gotKeys.append(key)
            else:
                self.gotKeys.append(
                    self.gotKeys.pop(self.gotKeys.index(key)))
            if len(self.gotKeys) > BaseCaching.MAX_ITEMS:
                discard = self.gotKeys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """return the value in self.cache_data linked to key
        """
        if key is not None and key in self.cache_data.keys():
            self.gotKeys.append(self.gotKeys.pop(self.gotKeys.index(key)))
            return self.cache_data.get(key)
        return None