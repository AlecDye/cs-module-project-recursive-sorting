# TO-DO: Implement a recursive implementation of binary search


def binary_search(
    arr, target, start, end,
):

    # case 1: base case (init the function)
    if end >= start:

        middle = (end + start) // 2

        # case 2: lucky guess if target is middle of array
        if arr[middle] == target:
            return middle

        # case 3: if target is less than middle, its in the left tree
        elif arr[middle] > target:
            return binary_search(arr, target, start, middle - 1)

        # case 4: if not case 3 this must be true (target is greater than middle therefore in the right tree)
        else:
            return binary_search(arr, target, middle + 1, end)

    else:
        # target not found in list
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
# def agnostic_binary_search(arr, target):
# Your code here

