# TO-DO: Complete the selection_sort() function below



# [1, 2, 4, 5, 6, 8, 9,             0, 3, 7]


def selection_sort(arr):
    # loop through n-1 elements
    # Divide your hand into sorted on the left and unsorted on the right 
    # Sorted is just the first element
    # Then go card by card and move them into place.
    # Loop through all elements in unsorted...
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here   
    for j in range(cur_index + 1, len(arr)): # j is our sliding index
        # Shift sorted to the right until correct position found
        if arr [j] < arr[smallest_index]:
            # Insert at that position
            smallest_index = j



        # TO-DO: swap
        # Your code here
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    indexing_length = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if arr[i] > arr[i+1]:
                sorted = False
                # Flip the values in list
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
