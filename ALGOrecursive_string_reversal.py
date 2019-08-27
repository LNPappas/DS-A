r = []

def reverse(string):
    global r
    if string == '':
        return str(''.join(r))
    r.append(string[-1])
    string = string[:-1]
    return reverse(string)

if __name__ == "__main__":
    s = "This is the string."
    print(reverse(s))

    print(s[::-1])