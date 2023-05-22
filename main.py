import random
import time
import matplotlib.pyplot as plt
import quicksort
import mergesort
import selectionsort
import bubblesort
import insertionsort
import concurrent.futures
selection_comparisons = []
bubble_comparisons = []
insertion_comparisons = []
merge_comparisons = []
quick_comparisons = []
quicktime = []
selectiontime = []
mergetime = []
insertiontime = []
bubbletime = []
# Generate the input values and sort using different algorithms
start = time.time()
for n in range(0, 5001, 100):

    with concurrent.futures.ThreadPoolExecutor() as exec:
        input_arr = [random.randint(0, 100) for i in range(n)]

        quicksort.i = n
        selection_comps = exec.submit(selectionsort.selection_sort, input_arr)
        bubble_comps = exec.submit(bubblesort.bubble_sort, input_arr)
        insertion_comps = exec.submit(insertionsort.insertion_sort, input_arr)
        quick_comps = exec.submit(quicksort.quick, input_arr)
        merge_comps = exec.submit(mergesort.mergee, input_arr)

        # Selection Sort
        selection_sort=selection_comps.result()
        selection_time =selection_sort[1]
        selectiontime.append(selection_time)
        selection_comparisons.append(selection_sort[0])

        # Bubble Sort
        bubble_sort =bubble_comps.result()
        bubble_time = bubble_sort[1]
        bubbletime.append(bubble_time)
        bubble_comparisons.append(bubble_sort[0])

        # Insertion Sort
        insertion_sort = insertion_comps.result()
        insertiontime.append(insertion_sort[1])
        insertion_comparisons.append(insertion_sort[0])

        # Merge Sort
        merge_sort = merge_comps.result()
        mergetime.append(merge_sort[1])
        merge_comparisons.append(merge_sort[0])

        # Quick Sort
        quick_sort = quick_comps.result()
        quicktime.append(quick_sort[1])
        quick_comparisons.append(quick_sort[0])

        print(
            f"n = {n}, Selection Comparisons and Time = {selection_comps.result()},Time = | Bubble Comparisons and Time = {bubble_comps.result()},Time = | "
            f"Insertion Comparisons and Time = {insertion_comps.result()},Time = | Merge Comparisons and Time = {merge_comps.result()},Time = | "
            f"Quick Comparisons and Time = {quick_comps.result()},Time = ")
end = time.time()
print(end-start)
# Plot the results
n_values = [i for i in range(0, 5001, 100)]
plt.figure("Fakher: Project Algorithm")
plt.plot(n_values, selection_comparisons, label='Selection Sort')
plt.plot(n_values, bubble_comparisons, label='Bubble Sort')
plt.plot(n_values, insertion_comparisons, label='Insertion Sort')
plt.plot(n_values, merge_comparisons, label='Merge Sort')
plt.plot(n_values, quick_comparisons, label='Quick Sort')
plt.xlabel('Input Size (n)')
plt.ylabel('Total Number of Element Comparisons')
plt.title('Sorting Algorithm Comparison')
plt.legend()
plt.show()
plt.figure("Fakher: Project Algorithm")
plt.plot(n_values, selectiontime, label='Selection Sort')
plt.plot(n_values, bubbletime, label='Bubble Sort')
plt.plot(n_values, insertiontime, label='Insertion Sort')
plt.plot(n_values, mergetime, label='Merge Sort')
plt.plot(n_values, quicktime, label='Quick Sort')
plt.xlabel('Input Size (n)')
plt.ylabel('Time')
plt.title('Sorting Algorithm Comparison')
plt.legend()
plt.show()
