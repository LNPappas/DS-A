import string
def LongestWord(sen): 

    sen = sen.translate(str.maketrans('','', "()/'!\@#$%^&*()_-+={[}]|\?.>,<`~:;"))
    l = sen.split(' ')
    longest = ''
    for x in l:
        if len(longest) < len(x):
            longest = x
    return longest

if __name__ == "__main__":
    print(LongestWord("What is the longest word in this string?"))
    print(LongestWord("fun&!! time"))