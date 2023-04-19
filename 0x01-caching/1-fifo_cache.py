from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.queue = []  # Initialize a list to keep track of the cache items

    def put(self, key, item):
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.queue.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}\n")

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
