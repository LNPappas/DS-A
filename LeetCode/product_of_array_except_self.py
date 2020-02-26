def productExceptSelf(nums):
    '''
        returns products of all elements of array 
        exculding current index
        w/o division
        O(n)
    '''

    # get the length of the list
    l = len(nums)
    # create list to hold results sams size as nums
    result = [0]*l
    # first element has nothing to it's left, so value is 1
    result[0] = 1

    # iterate through list recording all products to the left of element
    for i in range(1, l):
        # result[i] will record the product of all it's previous elements
        # and multiple them with the previous element of the array
        # so for the first round result[1] = 1*nums[0]
        # as you can see, this does not include the current value of i
        result[i] = result[i-1]*nums[i-1]

    # now we must do the same for the right values
    # we already have a list containing the left, so we only need a variable for the right
    # again since there is nothing to the right of the last element the first value = 1
    r = 1
    for i in reversed(range(l)):
        result[i] = result[i]*r 

        # we now need to multiply the current value of r with nums[i] for the next round
        r *= nums[i]

    return result


if __name__ == '__main__':
    print(productExceptSelf([1,2,3,4]))