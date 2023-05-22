import random
import time
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)
i = 0
arr = random.sample(range(1, i+1), i)
comparisons = [0] # to keep track of number of comparisons made

def mergesort_with_count(arr):


    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort_with_count(arr[:mid])
    right = mergesort_with_count(arr[mid:])
    merged = merge(left, right)
    comparisons[0] += len(merged)

    return merged
def mergee(arr):
    start_time = time.time()
    sorted_arr = mergesort_with_count(arr)
    end_time = time.time()
    merge_time = end_time - start_time
    return comparisons[0], merge_time