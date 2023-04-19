#!/usr/bin/python3
""" 1-main """
FIFOCache = __import__('1-fifo_cache').FIFOCache

class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.queue = []  # Initialize a list to keep track of the cache items

    def put(self, key, value):
        """
        Add a key-value pair to the cache.
        If the cache is full, remove the least recently added item.
        """
        if len(self.cache_data) >= self.MAX_ITEMS:
            oldest_key = self.queue.pop(0)
            del self.cache_data[oldest_key]

        self.cache_data[key] = value
        self.queue.append(key)

    def get(self, key):
        """
        Get a value from the cache for a given key.
        If the key is not in the cache, return None.
        """
        value = self.cache_data.get(key)
        if value is not None:
            self.queue.remove(key)
            self.queue.append(key)
        return value
