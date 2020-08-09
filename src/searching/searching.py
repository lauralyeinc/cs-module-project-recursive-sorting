# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # if the starting index is less than the ending index, return -1, break out
    if start > end:
        return -1 
    else:
        # this will find the midpoint
        mid_point = (start + end) // 2 # magic divide by 2 
        # if the target is equal to the midpoint, then return
        if target == arr[mid_point]:
            return mid_point
        # elifn the targer is less than mid_point, try the left side
        elif target < arr[mid_point]:
            # return the binary search with the mid_point and keeping consistent with the length of arr (-1)
            return binary_search(arr, target, start, mid_point-1)
        #if target is greater than mid_point, try the right side
        else:
            #return binary search with mid_point (+1)
            return binary_search(arr, target, end, mid_point+1)



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass 