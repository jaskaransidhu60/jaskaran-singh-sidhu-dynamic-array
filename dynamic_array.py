# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2: Dynamic Array and Bag ADT
# Description: Implements a Dynamic Array with additional operations including resizing, slicing, mapping, filtering, and reducing.

 from static_array import StaticArray

class DynamicArrayException(Exception):
    """Custom exception for DynamicArray errors"""
    pass

class DynamicArray:
    def __init__(self, start_array=None):
        """Initialize a dynamic array with a default capacity of 4, extendable as needed"""
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)
        
        # Append elements if provided a start array
        if start_array:
            for value in start_array:
                self.append(value)

    def __str__(self):
        """Return a string representation of the Dynamic Array for debugging"""
        values = ', '.join(str(self._data[i]) for i in range(self._size))
        return f"DYN_ARR Size/Cap: {self._size}/{self._capacity} [{values}]"

    def _resize(self, new_capacity):
        """Resize the underlying static array to the new capacity"""
        if new_capacity < self._size:
            return  # Do not reduce below current number of elements
        new_data = StaticArray(new_capacity)
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, value):
        """Add an element at the end, resizing if necessary"""
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = value
        self._size += 1

    def insert_at_index(self, index, value):
        """Insert an element at a specific index, shifting elements right and resizing if needed"""
        if index < 0 or index > self._size:
            raise DynamicArrayException("Invalid index")
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def remove_at_index(self, index):
        """Remove an element at a specific index, shifting elements left and resizing if capacity exceeds need"""
        if index < 0 or index >= self._size:
            raise DynamicArrayException("Invalid index")
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1
        if self._capacity > 10 and self._size < self._capacity // 4:
            self._resize(max(self._size * 2, 10))

    def get_at_index(self, index):
        """Return element at specific index"""
        if index < 0 or index >= self._size:
            raise DynamicArrayException("Invalid index")
        return self._data[index]

    def slice(self, start_index, size):
        """Return a new DynamicArray with elements from the start_index up to the specified size"""
        if start_index < 0 or size < 0 or start_index + size > self._size:
            raise DynamicArrayException("Invalid slice parameters")
        sliced_array = DynamicArray()
        for i in range(start_index, start_index + size):
            sliced_array.append(self._data[i])
        return sliced_array

    def map(self, map_func):
        """Return a new DynamicArray with each element mapped by the provided function"""
        mapped_array = DynamicArray()
        for i in range(self._size):
            mapped_array.append(map_func(self._data[i]))
        return mapped_array

    def filter(self, filter_func):
        """Return a new DynamicArray with only elements that satisfy the filter function"""
        filtered_array = DynamicArray()
        for i in range(self._size):
            if filter_func(self._data[i]):
                filtered_array.append(self._data[i])
        return filtered_array

    def reduce(self, reduce_func, initializer=None):
        """Reduce the array to a single value by applying the reduce function sequentially"""
        if self._size == 0:
            return initializer
        result = initializer if initializer is not None else self._data[0]
        start = 1 if initializer is None else 0
        for i in range(start, self._size):
            result = reduce_func(result, self._data[i])
        return result


# Standalone functions outside the class

def chunk(arr):
    """Chunk array into non-descending subarrays, returns a DynamicArray of DynamicArrays"""
    if arr._size == 0:
        return DynamicArray()
    chunks = DynamicArray()
    current_chunk = DynamicArray()
    current_chunk.append(arr.get_at_index(0))

    for i in range(1, arr._size):
        if arr.get_at_index(i) >= arr.get_at_index(i - 1):
            current_chunk.append(arr.get_at_index(i))
        else:
            chunks.append(current_chunk)
            current_chunk = DynamicArray()
            current_chunk.append(arr.get_at_index(i))
    chunks.append(current_chunk)
    return chunks

def find_mode(arr):
    """Find the mode(s) in a sorted DynamicArray"""
    if arr._size == 0:
        return DynamicArray(), 0
    mode_arr = DynamicArray()
    mode_count = 1
    current_count = 1
    current_val = arr.get_at_index(0)
    mode_arr.append(current_val)

    for i in range(1, arr._size):
        if arr.get_at_index(i) == current_val:
            current_count += 1
        else:
            if current_count > mode_count:
                mode_arr = DynamicArray()
                mode_arr.append(current_val)
                mode_count = current_count
            elif current_count == mode_count:
                mode_arr.append(current_val)
            current_val = arr.get_at_index(i)
            current_count = 1
    # Final check for last sequence
    if current_count > mode_count:
        mode_arr = DynamicArray()
        mode_arr.append(current_val)
        mode_count = current_count
    elif current_count == mode_count:
        mode_arr.append(current_val)
    return mode_arr, mode_count

