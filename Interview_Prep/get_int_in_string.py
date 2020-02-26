def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    if str == '':
        return 0

    def get_start(n):
        i = 0
        while i < len(n):
            if str[i] == ' ':
                i+=1
            else:
                return i
        return None

    start_index = get_start(str)
    if start_index == None:
        return 0

    l1 = str[start_index:].split()



    word = l1[0]
    l1 = [x for x in word]
    l2 = []
    if l1[0] == '-' or l1[0] == '+':
        l2 = [l1.pop(0)]
    if l1 == []:
        return 0
    if l1[0].isdigit() == False or l1 == []:
        return 0

    for x in l1:
        if x.isdigit() == True:
            l2.append(x)
        else:
            break
            
    num = int(''.join(l2))
    if num.bit_length() >= 32:
        if num > 0:
            return 2**31 -1
        else:
            return -2**31
    else:
        return num

if __name__ == "__main__":
    print(myAtoi('-'))
    print(myAtoi(' The words 123'))
    print(myAtoi('123 words 123'))
    print(myAtoi('    -123 words 123'))
    print(myAtoi('    123 words 123'))
    print(myAtoi('    123words 123'))
    print(myAtoi('    -.123 words 123'))
    print(myAtoi(' -The words 123'))
    print(myAtoi("   -42"))
    print(myAtoi(""))
    print(myAtoi(" "))
    print(myAtoi("+1"))
    print(myAtoi("2147483648"))
    print(myAtoi("-2147483648"))
    print(myAtoi("2147483647"))
    print(myAtoi("-2147483649"))
    print(myAtoi("2147483649"))

