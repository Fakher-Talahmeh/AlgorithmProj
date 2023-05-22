import random
import time
def selection_sort(arr):

    start_time = time.time()
    comparisons = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
            comparisons += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    end_time = time.time()
    selection_time = end_time - start_time
    return comparisons,selection_time
i=0
arr = random.sample(range(1, i+1), i)
comparisons = selection_sort(arr)
