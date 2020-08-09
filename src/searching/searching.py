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
    #sorted or not?, set up true or false if the array is in order
    # compare index 0 with index 1 of array
    if arr[0] > arr[-1]:
        is_ascending = False
    else:
        is_ascending = True
    # if the input array is ascending,c all 'binary_search' with the arry and target wanted
    if is_ascending:
        return binary_search(arr, target, 0 ,len(arr) - 1)
        #pass 
    # else call 
    else:
        return descending_binary_search(arr, target, 0, len(arr)-1)


#more practice, 😄
#setting up a desending_binary_search 
# lowest to highest 
def descending_binary_search(arr, target, left, right):
    #base case 
    if left > right:
        return -1 
    # this part is half done? the return above is keeping up with the lenght only, but not the index/elements. 
    else: 
        mid_point = (left + right) // 2

        if arr[mid_point] == target:
            return mid_point
        elif arr[mid_point] < target:
            return descending_binary_search(arr, target, left, mid_point -1)
        else: 
            return descending_binary_search(arr, target, mid_point + 1, right, )