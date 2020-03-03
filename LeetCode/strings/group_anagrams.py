def groupAnagrams(s):
    '''
        input: list of words
        output: list of words grouped in list by anagram
    '''
    # make dictionary to contain anagrams
    d = {}
    # iterate through list of words
    for word in s:
        # sort word and converst list back to string
        temp = ''.join(sorted(word))
        # if temp is already in d
        if temp in d:
            # get the list and append the new value
            y = d[temp]
            y.append(word)
            # set d[temp] to new list
            d[temp] = y
        else:
            # add temp as key and
            # list with word as value to d
            d[temp] = [word]
    # return a list with the lists in d
    return list(d.values())

if __name__ == "__main__":
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))