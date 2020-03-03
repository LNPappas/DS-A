from collections import Counter

def anagram(s,t):
    '''
        returns true if t is palindrom of s
    '''
    # dictionary to hold # repititions of value in s
    d = {}
    # iterate through s to fill d
    for x in s:
        # if elelment in d, increase by one
        # else add element to d with value 0 then increas by 1
        d[x] = d.get(s,0)+1
    # iterate through t to see if in s
    for x in t:
        # if element in d, decrease by one
        # else add element to d
        # default is 2 because 1 will be subtracted from value
        d[x] = d.get(x,2)-1
        if d[x] == 0:
            d.pop(x)
    # if d is empty return true
    return d == {}

def anagramCounter(s,t):
    '''
        returns true if t is palindrom of s
        uses collections class
        faster
    '''
    # if counters are equal, then anagram
    return Counter(s) == Counter(t)

if __name__ == "__main__":
    print(anagram("anagram", "nagaram"))
    print(anagramCounter("anagram", "nagaram"))
    print(anagram('a', 'ab'))
    print(anagramCounter('a', 'ab'))