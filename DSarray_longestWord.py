def LongestWord(sen): 

    s = iter(''.join(x for x in sen if x.isalpha() or x is ' '))
    current = longest = ''
    for x in s:
        if x == ' ':
            if len(longest) < len(current):
                longest = current 
            current = ''
        else:
            current += x
    if len(longest) < len(current):
        longest = current
    return longest

if __name__ == "__main__":
    print(LongestWord("What is the longest word in this string?"))
    print(LongestWord("fun&!! time"))