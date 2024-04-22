# Implementation of sorting algorithms and experimental comparison
import time
import random


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


pass


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    pass


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    pass


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    pass


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
    pass


def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    pass


# Generate random dataset for experimentation
dataset_size = 10000
random_data = [random.randint(1, 100000) for _ in range(dataset_size)]
print(random_data)

# Measure execution time for each sorting algorithm
start_time = time.time()
bubble_sort(random_data.copy())
bubble_sort_execution_time = time.time() - start_time
print(f"Bubble Sort Execution Time: {bubble_sort_execution_time:.6f} seconds")

start_time = time.time()
selection_sort(random_data.copy())
selection_sort_execution_time = time.time() - start_time
print(f"Selection Sort Execution Time: {selection_sort_execution_time:.6f} seconds")

start_time = time.time()
insertion_sort(random_data.copy())
insertion_sort_execution_time = time.time() - start_time
print(f"Insertion Sort Execution Time: {insertion_sort_execution_time:.6f} seconds")

start_time = time.time()
merge_sort(random_data.copy())
merge_sort_execution_time = time.time() - start_time
print(f"Merge Sort Execution Time: {merge_sort_execution_time:.6f} seconds")

start_time = time.time()
quick_sort(random_data.copy())
quick_sort_execution_time = time.time() - start_time
print(f"Quick Sort Execution Time: {quick_sort_execution_time:.6f} seconds")

start_time = time.time()
heap_sort(random_data.copy())
heap_sort_execution_time = time.time() - start_time
print(f"Heap Sort Execution Time: {heap_sort_execution_time:.6f} seconds")
