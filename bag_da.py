# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2: Bag ADT
# Description: Implements a Bag ADT using a Dynamic Array.

from dynamic_array import DynamicArray, DynamicArrayException

class Bag:
    def __init__(self, start_bag=None):
        """
        Initialize a new bag using a DynamicArray.
        """
        self._da = DynamicArray()
        # Populate bag with initial values if provided
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return the content of the bag in a human-readable form.
        """
        out = "BAG: " + str(self.size()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(i)) for i in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return the number of elements in the bag.
        """
        return self._da.length()

    def add(self, value: object) -> None:
        """
        Add a new element to the bag.
        """
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        Remove one instance of a specified element from the bag.
        """
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                self._da.remove_at_index(i)
                return True
        return False

    def count(self, value: object) -> int:
        """
        Count the number of instances of a specified element in the bag.
        """
        count = 0
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                count += 1
        return count

    def clear(self) -> None:
        """
        Clear all elements from the bag.
        """
        self._da = DynamicArray()  # Reinitialize with an empty DynamicArray

    def equal(self, second_bag: "Bag") -> bool:
        """
        Check if two bags have the same elements (order does not matter).
        """
        if self.size() != second_bag.size():
            return False
        checked_indices = set()
        for i in range(self._da.length()):
            item = self._da.get_at_index(i)
            if self.count(item) != second_bag.count(item):
                return False
        return True

    def __iter__(self):
        """
        Return an iterator for the bag.
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Return the next element in the bag during iteration.
        """
        if self._index < self._da.length():
            value = self._da.get_at_index(self._index)
            self._index += 1
            return value
        else:
            raise StopIteration
