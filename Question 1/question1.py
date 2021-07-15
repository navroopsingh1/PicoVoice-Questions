from collections import OrderedDict
from typing import List

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if not key in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

def get_book_info(isbn):
    pass

def get_book_info_wrapper(isbn : str, cache: LRUCache) -> List[str, str, str]:
    cache.set(isbn, get_book_info(isbn))
    return cache.get(isbn)
