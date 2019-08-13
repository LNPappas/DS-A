import string

def LongestWord(sen): 

    exclude = set(string.punctuation)
    s = ''.join(x for x in sen if x not in exclude)
    s = iter(s)
    longest = ''
    current = ''
    for x in s:
        if x != ' ':
            current += x
        longest = max(len(longest), len(current))
        if x == ' ':
            current = ''
    
    return longest

if __name__ == "__main__":
    print(LongestWord("What is the longest word in this string?"))