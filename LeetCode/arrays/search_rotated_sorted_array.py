def search(array, target):
    '''
        takes a rotated sorted array and returns index of target element
        returns -1 if target not in array
        O(logn) <- binary search 
    '''
    # if the array is empty return -1:
    if not array:
        return -1
    # set left pointer at start and right pointer at n
    left, right = 0, len(array)-1

    # keep going until left and right pointer meet
    while left <= right:
        # calculate mid of array/subarray:
        m = (left+right)//2 # don't forget order of oppurations!!
        # if the m is the target return it's index
        if array[m] == target:
            return m
        # otherwise value at left <= value at m:
        if array[left] <= array[m]:
            # if the target is between left and m, set right as m-1
            if array[left] <= target <= array[m]:
                right = m-1
            #otherwise it's in the other half of the (sub)array:
            else:
                left = m+1
        # last if array[m] > target:
        else:
            # check if target between m and right:
            if array[m] <= target <= array[right]:
                # if target btwn m and right, set m to left
                left = m+1
            # else set m to right cause it's in the other half of the (sub)array
            else:
                right = m-1
    # if the target is not in the array return -1
    return -1



if __name__ == "__main__":
    print(search([4,5,6,7,0,1,2],5))
    print(search([4,5,6,7,0,1,2],0))
    print(search([4,5,6,7,0,1,2],3))
