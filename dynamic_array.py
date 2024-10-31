# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2: Dynamic Array and Bag ADT
# Description: Implements a Dynamic Array with additional operations including resizing, slicing, mapping, filtering, and reducing.

 
class DynamicArrayException(Exception):
    """Custom exception class to be used by Dynamic Array"""
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)
        
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[i]) for i in range(self._size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        if index < 0 or index >= self._size:
            raise DynamicArrayException("Index out of bounds")
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        if index < 0 or index >= self._size:
            raise DynamicArrayException("Index out of bounds")
        self._data[index] = value

    def is_empty(self) -> bool:
        return self._size == 0

    def length(self) -> int:
        return self._size

    def get_capacity(self) -> int:
        return self._capacity

    def resize(self, new_capacity: int) -> None:
        if new_capacity <= 0 or new_capacity < self._size:
            return
        
        new_data = StaticArray(new_capacity)
        for i in range(self._size):
            new_data[i] = self._data[i]
        
        self._capacity = new_capacity
        self._data = new_data

    def append(self, value: object) -> None:
        if self._size == self._capacity:
            self.resize(2 * self._capacity)
        self._data[self._size] = value
        self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        if index < 0 or index > self._size:
            raise DynamicArrayException("Index out of bounds")
        
        if self._size == self._capacity:
            self.resize(2 * self._capacity)
        
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        
        self._data[index] = value
        self._size += 1

    def remove_at_index(self, index: int) -> None:
        if index < 0 or index >= self._size:
            raise DynamicArrayException("Index out of bounds")
        
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        
        self._size -= 1
        
        if self._size < self._capacity // 4 and self._capacity > 10:
            new_capacity = max(self._size * 2, 10)
            self.resize(new_capacity)

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        if start_index < 0 or start_index >= self._size or size < 0 or (start_index + size) > self._size:
            raise DynamicArrayException("Invalid slice parameters")
        
        new_array = DynamicArray()
        for i in range(start_index, start_index + size):
            new_array.append(self._data[i])
        return new_array

    def map(self, map_func) -> "DynamicArray":
        new_array = DynamicArray()
        for i in range(self._size):
            new_array.append(map_func(self._data[i]))
        return new_array

    def filter(self, filter_func) -> "DynamicArray":
        new_array = DynamicArray()
        for i in range(self._size):
            if filter_func(self._data[i]):
                new_array.append(self._data[i])
        return new_array

    def reduce(self, reduce_func, initializer=None) -> object:
        if self.is_empty():
            return initializer

        result = initializer if initializer is not None else self._data[0]
        start = 0 if initializer is not None else 1

        for i in range(start, self._size):
            result = reduce_func(result, self._data[i])
        
        return result


# Standalone functions
def chunk(arr: DynamicArray) -> DynamicArray:
    if arr.is_empty():
        return DynamicArray()
    
    result = DynamicArray()
    chunk_array = DynamicArray()
    chunk_array.append(arr.get_at_index(0))

    for i in range(1, arr.length()):
        if arr.get_at_index(i) >= arr.get_at_index(i - 1):
            chunk_array.append(arr.get_at_index(i))
        else:
            result.append(chunk_array)
            chunk_array = DynamicArray()
            chunk_array.append(arr.get_at_index(i))
    
    result.append(chunk_array)
    return result

def find_mode(arr: DynamicArray) -> tuple:
    if arr.is_empty():
        return DynamicArray(), 0
    
    mode_array = DynamicArray()
    max_count = 1
    current_count = 1
    mode_array.append(arr.get_at_index(0))

    for i in range(1, arr.length()):
        if arr.get_at_index(i) == arr.get_at_index(i - 1):
            current_count += 1
        else:
            current_count = 1

        if current_count > max_count:
            max_count = current_count
            mode_array = DynamicArray()
            mode_array.append(arr.get_at_index(i))
        elif current_count == max_count:
            mode_array.append(arr.get_at_index(i))
    
    return mode_array, max_count
