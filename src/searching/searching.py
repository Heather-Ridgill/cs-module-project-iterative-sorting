def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # search space is arr[left to right]
    (left, right) = (0, len(arr) - 1)

    # till search space consists of at-least one element
    while left <= right:

        # we find the mid value in the search space and
        # compares it with key value

        mid = (left + right) // 2

        # overflow can happen. Use:
        # mid = left + (right - left) / 2
        # mid = right - (right - left) // 2

        # key value is found
        if target == arr[mid]:
            return mid

        # discard all elements in the right search space
        # including the mid element
        elif target < arr[mid]:
            right = mid - 1

        # discard all elements in the left search space
        # including the mid element
        else:
            left = mid + 1

    # x doesn't exist in the list
    return -1

