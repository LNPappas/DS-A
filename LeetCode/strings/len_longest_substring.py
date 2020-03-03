def subString(s):
    '''
        Takes a string
        returns length of longest substring
        O(n)
    '''
    # if empty string return 0
    if not s:
        return 0
    # dictionary to hold past letters:
    d = {}
    # start pointer for beginning of current substring
    start = 0
    # result variable for longest substring length
    result = 0
    # iterate through the string
    for index, value in enumerate(s):
        # if the value is not in the dictionary or 
        # if the value is in the dictionary before the start pointer
        if value not in d or d[value] < start:
            # result = highest length including result itself
            # and the current index - starting index + 1(because starts at 0)
            result = max(result, index-start+1)
        # otherwise
        else:
            # move starting pointer to 1 past where the repeated value is 
            start = d[value]+1
        # add/reasign current value and index in dictionary
        d[value] = index
    return result
        
if __name__ == "__main__":
    print(subString("abcabcbb"))
    print(subString("bbbbb"))
    print(subString("pwwkew"))
    print(subString(''))
    print(subString(' '))