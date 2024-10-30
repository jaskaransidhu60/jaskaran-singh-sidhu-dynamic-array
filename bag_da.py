# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2: Dynamic Array and ADT Implementation
# Description: Implements a Bag ADT using a Dynamic Array for storage.

from dynamic_array import *

class Bag:
    def __init__(self, start_bag=None):
        """Initialize a new Bag."""
        self._da = DynamicArray()

        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """Return a human-readable representation of the Bag."""
        return f"BAG: {self._da.length()} elements. [{', '.join(str(self._da[i]) for i in range(self._da.length()))}]"

    def add(self, value: object) -> None:
        """Add a value to the Bag."""
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """Remove one occurrence of the value from the Bag."""
        for i in range(self._da.length()):
            if self._da[i] == value:
                self._da.remove_at_index(i)
                return True
        return False

    def count(self, value: object) ->
