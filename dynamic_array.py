# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2: Dynamic Array and Bag ADT
# Description: Implements a Dynamic Array with additional operations including resizing, slicing, mapping, filtering, and reducing.

from static_array import StaticArray

class DynamicArrayException(Exception):
    """
    Custom exception class to handle invalid operations on the Dynamic Array.
    """
    pass

class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize a new dynamic array with initial capacity 4.
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # Populate dynamic array with initial values if provided
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form.
        """
        out = f"DYN_ARR Size/Cap: {self._size}/{self._capacity} ["
        out += ', '.join([str(self._data[i]) for i in range(self._size)])
        return out + ']'

    def resize(self, new_capacity: int) -> None:
        """
        Resize the internal storage of the array.
        """
        if new_capacity < self._size:
            return
        new_data = StaticArray(new_capacity)
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, value: object) -> None:
        """
        Add a value to the end of the array.
        """
        if self._size == self._capacity:
            self.resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Insert a value at a specific index in the array.
        """
        if index < 0 or index > self._size:
            raise DynamicArrayException("Index out of range")
        if self._size == self._capacity:
            self.resize(self._capacity * 2)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def remove_at_index(self, index: int) -> None:
        """
        Remove the element at the specified index.
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException("Index out of range")
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1
        if self._size < self._capacity // 4 and self._capacity > 4:
            new_capacity = max(self._capacity // 2, 4)
            self.resize(new_capacity)

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Return a slice of the array.
        """
        if start_index < 0 or size < 0 or start_index + size > self._size:
            raise DynamicArrayException("Invalid slice parameters")
        result = DynamicArray()
        for i in range(start_index, start_index + size):
            result.append(self._data[i])
        return result

    def map(self, map_func) -> "DynamicArray":
        """
        Apply a function to all elements and return a new array.
        """
        result = DynamicArray()
        for i in range(self._size):
            result.append(map_func(self._data[i]))
        return result

    def filter(self, filter_func) -> "DynamicArray":
        """
        Filter elements based on a function and return a new array.
        """
        result = DynamicArray()
        for i in range(self._size):
            if filter_func(self._data[i]):
                result.append(self._data[i])
        return result

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Reduce the array to a single value using the provided function.
        """
        if self._size == 0 and initializer is None:
            return None
        result = initializer if initializer is not None else self._data[0]
        start_index = 0 if initializer is not None else 1
        for i in range(start_index, self._size):
            result = reduce_func(result, self._data[i])
        return result

def chunk(arr: DynamicArray) -> DynamicArray:
    """
    Separate an array into chunks of non-decreasing subsequences.
    """
    result = DynamicArray()
    if arr.length() == 0:
        return result
    chunk = DynamicArray([arr[0]])
    for i in range(1, arr.length()):
        if arr[i] >= arr[i - 1]:
            chunk.append(arr[i])
        else:
            result.append(chunk)
            chunk = DynamicArray([arr[i]])
    result.append(chunk)
    return result

def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
    """
    Find the mode(s) in a sorted array and return it along with its frequency.
    """
    if arr.length() == 0:
        return DynamicArray(), 0
    mode = DynamicArray([arr[0]])
    max_count = current_count = 1
    current_value = arr[0]
    for i in range(1, arr.length()):
        if arr[i] == current_value:
            current_count += 1
        else:
            if current_count > max_count:
                mode = DynamicArray([current_value])
                max_count = current_count
            elif current_count == max_count:
                mode.append(current_value)
            current_value = arr[i]
            current_count = 1
    if current_count > max_count:
        return DynamicArray([current_value]), current_count
    if current_count == max_count:
        mode.append(current_value)
    return mode, max_count
