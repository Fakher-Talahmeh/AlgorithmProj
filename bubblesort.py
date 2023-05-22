import random
import time
def bubble_sort(arr):

    start_time = time.time()
    n = len(arr)
    comparisons = 0
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            comparisons += 1

    end_time = time.time()
    bubble_time = end_time - start_time
    return comparisons,bubble_time
i=0
arr = random.sample(range(1, i+1), i)
comparisons = bubble_sort(arr)
