# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    # Your code here
    # labels to hold current index. start at 0, because the smallest ends of both lists are 0.  (one list could be empty, we always start with 0 index as well). checked the test and the lists are sorted (thank you!).
    left_index = 0
    right_index = 0

    #store the length of two inputs in a new variable to keep code cleaner, not repeating myself. 
    leftArr = len(arrA)
    rightArr = len(arrB)

    # setting up the final output 
    merged_arr = []

    # we are using a while loop, to compare each side and until we used up all elments in each/or one of the lists. (may be odd numbered)

    while (left_index < leftArr) and (right_index < rightArr):
        #compare the elements at top of each list and append whichever is smallest to merged list.
        if (arrA[left_index] < arrB[right_index]):
            merged_arr.append(arrA[left_index])
            # increment on the index from the list (left) we just appended from, to prevent an infintiy loop. 
            left_index += 1 
        # if the left index in the arrA (left) is not greater than the right index in arrB (right) we are going to append that element into the merged_list and again, icrement the index to keep from being stuck in a loop
        else:
            merged_arr.append(arrB[right_index])
            right_index += 1 
    # we extend the merged list with whichever of the lists that wasn't completly empty ( or looped thru)
    if left_index == leftArr:
        merged_arr.extend(arrB[right_index:])
    else:
        merged_arr.extend(arrA[left_index:])
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # a list with only 1 element or less is already sorted...
    if len(arr) <= 1:
        return arr
    # divide the length of the arr by // 2 
    divided_len = len(arr) // 2

    # we can now call merge_sorted recursively on each half of the arr
    left_Arr = merge_sort(arr[:divided_len]) # starts at the begining of the arr and stops at the middle. slicing?
    right_Arr = merge_sort(arr[divided_len:]) #starts at the middle and stops when the list is none/empty. not hard coded. 

    # merge the two lists with the merge function
    arr = merge(left_Arr, right_Arr)
    
    return arr
    #pass 

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass 

