# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2: Bag ADT
# Description: Implements a Bag ADT that allows duplicates using a DynamicArray for underlying storage.

from dynamic_array import DynamicArray, DynamicArrayException

class Bag:
    def __init__(self, start_bag=None):
        """
        Initialize a new bag based on DynamicArray.
        """
        self._da = DynamicArray()
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of bag in human-readable form.
        """
        out = f"BAG: {self._da.length()} elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def add(self, value: object) -> None:
        """
        Add a value to the bag.
        """
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        Remove any one occurrence of value from the bag.
        """
        for i in range(self._da.length()):
            if self._da[i] == value:
                self._da.remove_at_index(i)
                return True
        return False

    def count(self, value: object) -> int:
        """
        Count the number of occurrences of a value in the bag.
        """
        count = 0
        for i in range(self._da.length()):
            if self._da[i] == value:
                count += 1
        return count

    def clear(self) -> None:
        """
        Clear all elements from the bag.
        """
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """
        Check if two bags have the same elements in any order.
        """
        if self._da.length() != second_bag._da.length():
            return False
        for i in range(self._da.length()):
            if self.count(self._da[i]) != second_bag.count(self._da[i]):
                return False
        return True

    def __iter__(self):
        """
        Initialize the iterator.
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Return the next item in the bag.
        """
        if self._index >= self._da.length():
            raise StopIteration
        result = self._da[self._index]
        self._index += 1
        return result
