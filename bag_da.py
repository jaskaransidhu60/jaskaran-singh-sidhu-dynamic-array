# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2: Bag ADT
# Description: Implements a Bag ADT using a Dynamic Array.

class Bag:
    def __init__(self, start_bag=None):
        self._da = DynamicArray()
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        out = "BAG: " + str(self.size()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(i)) for i in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        return self._da.length()

    def add(self, value: object) -> None:
        self._da.append(value)

    def remove(self, value: object) -> bool:
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                self._da.remove_at_index(i)
                return True
        return False

    def count(self, value: object) -> int:
        count = 0
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                count += 1
        return count

    def clear(self) -> None:
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        if self.size() != second_bag.size():
            return False

        for i in range(self._da.length()):
            value = self._da.get_at_index(i)
            if self.count(value) != second_bag.count(value):
                return False
        return True

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < self._da.length():
            value = self._da.get_at_index(self._index)
            self._index += 1
            return value
        else:
            raise StopIteration
