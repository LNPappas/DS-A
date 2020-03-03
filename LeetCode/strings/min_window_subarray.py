from collections import Counter

def minWindow(s, t):
    '''
        function finds smallest length of substring
        in s that contains all values of t
        both strings are all capital letters
        returns substring
        O(n)
    '''
    # import counter from collections
    # determine how many of each value is needed
    # creates dictionary with keys as value 
    # in t and values as times occur in t
    need = Counter(t)
    # determine total # of all values needed
    missing = sum(need.values())
    # create varaible for result string, default empty
    result = ""
    # create variabel for length of result, default high number
    result_len = float('inf')
    # create pointer for start of subarray, starting at beginning of s
    left = 0
    # iterate through array, current index = right pointer/end of subarray
    for right in range(len(s)):
        # if the value at the current index is needed
        if s[right] in need:
            # decrease # of missing values
            # need[s[right]] > 0 is boolean statement. 1 for true zero for false
            missing -= need[s[right]] > 0
            # decrease the needed values for that character
            need[s[right]] -= 1
            # if no values are missing
            while missing == 0:
                # if current substring length < result substring length
                # reult substring length = current substring length
                if right-left+1 < result_len:
                    result_len = right-left+1
                    # result substring = current substring
                    result = s[left:right+1]
                # if the left value is in t
                if s[left] in need:
                    # increase the value of chars missing
                    missing += need[s[left]] >= 0
                    # the # of missing elements for that character
                    need[s[left]] += 1
                # move the left pointer forward 1 index
                left += 1
    return result

if __name__ == "__main__":
    print(minWindow("ADOBECODEBANC", 'ABC'))