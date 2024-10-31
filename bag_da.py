# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2: Bag ADT
# Description: Implements a Bag ADT using a Dynamic Array.

from dynamic_array import DynamicArray, DynamicArrayException

class Bag:
    def __init__(self, start_bag=None):
        """Initialize the Bag with elements if provided"""
        self._da = DynamicArray()
        if start_bag:
            for value in start_bag:
                self.add(value)

    def __str__(self):
        """String representation of the Bag"""
        items = ', '.join(str(self._da.get_at_index(i)) for i in range(self._da.length()))
        return f"BAG: {self.size()} elements. [{items}]"

    def size(self):
        """Return number of items in Bag"""
        return self._da.length()

    def add(self, value):
        """Add item to Bag"""
        self._da.append(value)

    def remove(self, value):
        """Remove one instance of value from Bag if it exists"""
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                self._da.remove_at_index(i)
                return True
        return False

    def count(self, value):
        """Count occurrences of value in Bag"""
        count = 0
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                count += 1
        return count

    def clear(self):
        """Clear all items from the Bag"""
        self._da = DynamicArray()

    def equal(self, other_bag):
        """Check if two Bags contain the same items with the same frequencies"""
        if self.size() != other_bag.size():
            return False
        for i in range(self._da.length()):
            if self.count(self._da.get_at_index(i)) != other_bag.count(self._da.get_at_index(i)):
                return False
        return True

    def __iter__(self):
        """Create an iterator for the Bag"""
        self._index = 0
        return self

    def __next__(self):
        """Iterate over elements in the Bag"""
        if self._index < self._da.length():
            result = self._da.get_at_index(self._index)
            self._index += 1
            return result
        else:
            raise StopIteration
