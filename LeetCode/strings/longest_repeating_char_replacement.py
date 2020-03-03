def charReplace(s, k):
    '''
        given k char replacements
        replace the character resulting in the 
        longest substring of repeated characters
        O(n)
    '''
    # create a dictionary that contains the amount char
    # and the # times it is repeated in current substring
    char_count = {}
    # create variables for max repeating char, 
    # the starting pointer, and the result
    max_char = start = result = 0
    # iterate through entire string
    # the index of which is the end of the substring
    for end in range(len(s)):
        # increase the count of the char at the current index
        # if it is in the dictionary
        # else add it to the dictionary and increase it's count
        char_count[s[end]] = char_count.get(s[end], 0) + 1
        # now that count is increased, see if it is the highest count
        # if so update make max_char
        max_char = max(max_char, char_count[s[end]])
        # if the lenght of the current subarray - maximum charater count
        # is > then alloted changes
        # remember to add one to start to account for index 0
        if end - start+1 - max_char > k:
            # decrease the starting pointer count value by one and
            # move the starting pointer to the next value
            char_count[s[start]] -= 1
            start +=1
        # if the length of the current sub array is longer
        # then the previous longest sub array
        # update the result to the current length
        result = max(result, end-start+1)
    return result 


if __name__ == "__main__":
    print(charReplace("ABAB", 2))
    print(charReplace("AABABBA", 1))