import sys
def minArray(array):
    '''
        find the min element in a rotated array
        O(logn) <- binary search
    '''
    # create a left pointer at the start of the array
    left = 0
    # create a right pointer at the end of the array
    right = len(array)-1
    # give result a really big number
    result = sys.maxsize

    # each loop cuts the array in half until we have a result
    while left <= right:
        # mid = the middle or average
        # take the floor so it is an int
        # make sure you use parathesis or you're fucked
        mid = (left+right)//2
        # we can use mid() here because it's O(2) == O(1)
        result = min(result, array[mid])
        # if array[mid] is less then mid, than mid is to the right
        if array[mid] <= array[right]:
            right = mid-1
        # otherwise min is to the left
        else:
            left = mid+1

    # return the minimum element
    return result


if __name__ == "__main__":
    print(minArray([2,1]))
    print(minArray([1,2,3]))
    print(minArray([3,4,5,1,2]))
