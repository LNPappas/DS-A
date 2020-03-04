def maxSubarray(array):
    '''
        this function returns the highest value
        calculated by the sume of a subarray 
        from of a given array.
        O(n)
    '''
    if not array:
        return 0
    # create variable for current value in array and 
    # the maximum value so far (the result)
    # set to first element of array
    current = array[0]
    result = array[0]

    # iterate array starting from index 1:
    for i in range(1,len(array)):
        # if the current value is greater than zero, add the array[i] value
        if current > 0:
            current = current + array[i]
        # else restart the sum of sub array at the array[i] value
        else:
            current = array[i]
        # if the current value is greater then the result or max value
        # make the max value the current value
        if current > result:
            result = current
    # return the max value of the entire array
    return result

if __name__ == "__main__":
    print(maxSubarray([-2,1,-3,4,-1,2,1,-5,4]))