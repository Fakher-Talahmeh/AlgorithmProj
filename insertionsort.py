import random
import time
def insertion_sort(arr):

    start_time = time.time()
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            comparisons += 1
        arr[j+1] = key
    end_time= time.time()
    insertion_time = end_time - start_time
    return comparisons,insertion_time
i=0
arr = random.sample(range(1, i+1), i)