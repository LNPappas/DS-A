def twoSum(target, array):
    '''
        returns indicies of first two number that add
        up to target. 
    '''
    # create dictionary to hold possible numbers
    d = {}

    # iterate through list to begin finding numbers
    for index, value in enumerate(array):
        # if value in dictionary, return stored index and current index
        if value in d:
            return [d[value], index]
        # else add value:index of counter part to d
        else:
            d.update({target-value:index})
        
    # if no numbers meet criteria return "none"
    return 'none'

if __name__ == "__main__":
    print(twoSum(9, [2,7,11,15]))