import random
import time
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = []
        equal = []
        greater = []
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
i=0
arr = random.sample(range(1, i+1), i)
comparisons = [0] # to keep track of number of comparisons made
def quicksort_with_count(arr):

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = []
        equal = []
        greater = []
        for x in arr:
            comparisons[0] += 1
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        return quicksort_with_count(less) + equal + quicksort_with_count(greater)

def quick(arr):
    start_time = time.time()
    sorted_arr = quicksort_with_count(arr)
    end_time = time.time()
    quick_time = end_time - start_time
    return comparisons[0],quick_time
