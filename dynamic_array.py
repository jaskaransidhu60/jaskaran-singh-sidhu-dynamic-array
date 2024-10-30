# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2: Dynamic Array and ADT Implementation
# Due Date: 10/28/2024
# Description: Implements a Dynamic Array with additional operations including 
# resizing, slicing, filtering, and reducing, used to build a Bag ADT.

from static_array import StaticArray

class DynamicArrayException(Exception):
    """Custom exception to handle invalid operations on the Dynamic Array."""
    pass

class DynamicArray:
    def __init__(self, start_array=None):
        """Initialize a new dynamic array."""
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """Return a human-readable representation of the array."""
        out = f"DYN_ARR Size/Cap: {self._size}/{self._capacity} ["
        out += ', '.join([str(self._data[i]) for i in range(self._size)])
        return out + ']'

    def resize(self, new_capacity: int) -> None:
        """Resize the internal storage of the array."""
        if new_capacity < self._size:
            return

        new_data = StaticArray(new_capacity)
        for i in range(self._size):
            new_data[i] = self._data[i]

        self._data = new_data
        self._capacity = new_capacity

    def append(self, value: object) -> None:
        """Add a value to the end of the array."""
        if self._size == self._capacity:
            self.resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """Insert a value at a specific index."""
        if index < 0 or index > self._size:
            raise DynamicArrayException()

        if self._size == self._capacity:
            self.resize(self._capacity * 2)

        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]

        self._data[index] = value
        self._size += 1

    def remove_at_index(self, index: int) -> None:
        """Remove the element at the given index."""
        if index < 0 or index >= self._size:
            raise DynamicArrayException()

        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]

        self._size -= 1

        if self._size < self._capacity // 4 and self._capacity > 4:
            self.resize(max(self._capacity // 2, 4))

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """Return a slice of the array."""
        if start_index < 0 or size < 0 or start_index + size > self._size:
            raise DynamicArrayException()

        result = DynamicArray()
        for i in range(start_index, start_index + size):
            result.append(self._data[i])
        return result

    def map(self, map_func) -> "DynamicArray":
        """Apply a function to all elements and return a new array."""
        result = DynamicArray()
        for i in range(self._size):
            result.append(map_func(self._data[i]))
        return result

    def filter(self, filter_func) -> "DynamicArray":
        """Filter elements based on a function and return a new array."""
        result = DynamicArray()
        for i in range(self._size):
            if filter_func(self._data[i]):
                result.append(self._data[i])
        return result

    def reduce(self, reduce_func, initializer=None) -> object:
        """Reduce the array to a single value using the provided function."""
        if self._size == 0 and initializer is None:
            return None

        result = initializer if initializer is not None else self._data[0]
        start = 0 if initializer is not None else 1

        for i in range(start, self._size):
            result = reduce_func(result, self._data[i])

        return result

    def length(self) -> int:
        """Return the number of elements in the array."""
        return self._size

    def get_capacity(self) -> int:
        """Return the current capacity of the array."""
        return self._capacity

# ------------------- BASIC TESTING -----------------------------------------
if __name__ == "__main__":
    da = DynamicArray([1, 2, 3])
    print(da)

    da.append(4)
    print(da)

    da.insert_at_index(1, 99)
    print(da)

    da.remove_at_index(2)
    print(da)

    sliced = da.slice(1, 2)
    print(sliced)

    mapped = da.map(lambda x: x * 2)
    print(mapped)

    filtered = da.filter(lambda x: x > 2)
    print(filtered)

    result = da.reduce(lambda x, y: x + y, 0)
    print(result)
