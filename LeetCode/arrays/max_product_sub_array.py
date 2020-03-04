def maxProduct(array):
    '''
        Function returns the maximum product of a continuous
        subarray with the largest product.
        Array contains at least one number
        O(n)
    '''
    # create variables for current highest product, current lowest product, 
    # and highest product thus far(the final result)
    # set them equal to first element of array
    high = low = result = array[0]

    # iterate through rest of the array to see all elements
    for i in range(1,len(array)):
        # create a temporart list to compare current elements
        # include the product of the current value of the array 
        # with the product of the high value, the low value 
        # and the element itself incase it is higher then any other
        temp = [array[i], array[i]*high, array[i]*low]
        # set the new high to the max of temp
        high = max(temp)
        # set the new low to the min of temp (we need the low value in
        # case the subarray, though lower now, is eventually 
        # higher with additional elements)
        low = min(temp)
        # the result (or highest value of all) should be whatever is 
        # currenly the highest value high > result
        result = max(high, result)

    # return the highest product of subarray
    return result

if __name__ == "__main__":
    print(maxProduct([2,3,-2,4]))
    print(maxProduct([-2,0,-1]))
    print(maxProduct([-4,-3,-2]))