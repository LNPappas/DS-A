def three(array):
    '''
        returns a list of lists with 3 values where sum(list) = 0
        no duplicate lists
        O(n^2)
    '''
    # if there are not 3 values in the list then there's no solutions
    if len(array) < 3:
        return []
    # otherwise sort the list:
    array.sort()
    # have a result that only contains unique answers
    result = set()
    # run through the list not including it's last element
    # we will use i+1 and want to keep index in range
    for index, value in enumerate(array[:-2]):
        # we don't care about duplicate values so
        # if the next previous is the same, pass.
        if index >= 1 and value == array[index-1]:
            continue
        # create a dictionary to key of third value looking for
        d = {}
        # we need to keep searching the list for the next two values
        # but we don't care about any previous values
        for v in array[index+1:]: # this is where we would go out of range if not array[:-2]
            # if the value is not in the dictionary, then we're not searching for it
            # but it could still be part of a set of 3 with previous value
            # so add a search for the value that would make value + v == 0
            # so essentially 0-value-v
            if v not in d:
                d[-value-v] = 1 # here the 1 doesn't matter, we only need the key
            # if v is in d, then we have our third value
            else:
                # so add all three to the result
                # we know the middle value, because it's 0 minus the other two values
                result.add((value, -value-v, v)) # remember your putting a tuple (value, -value-v, v) into result.add()
                # we don't remove if from the dictionary because set() will take care of duplicates
    # now we have a set of sets to return, but we need a lsit of lists
    # return the list of the map of the result set to list
    return list(map(list, result)) # without external list() it returns map object

if __name__ == '__main__':
    print(three([-1,0,1,2,-1,-4]))
    print(three([]))

    