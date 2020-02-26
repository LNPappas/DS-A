def containsDuplicates(array):
    '''
        boolean function that returns True if 
        their are any duplicates in given array
    '''
    # if the length of the array is greater than
    # the length of the set of the array
    # then the array contains duplicates
    return len(array) > len(set(array))

if __name__ == "__main__":
    print(containsDuplicates([1,2,3,1]))
    print(containsDuplicates([1,2,3,4])) 