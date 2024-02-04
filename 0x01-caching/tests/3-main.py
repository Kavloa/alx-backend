#!/usr/bin/python3
""" 3-main """
LRUCache = __import__('3-lru_cache').LRUCache

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))

my_cache.put("E", "Battery")
my_cache.print_cache()

my_cache.put("C", "Street")
my_cache.print_cache()

print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))

my_cache.put("F", "Mission")
my_cache.print_cache()

my_cache.put("G", "San Francisco")
my_cache.print_cache()

my_cache.put("H", "H")
my_cache.print_cache()

my_cache.put("I", "I")
my_cache.print_cache()

my_cache.put("J", "J")
my_cache.print_cache()

my_cache.put("K", "K")
my_cache.print_cache()