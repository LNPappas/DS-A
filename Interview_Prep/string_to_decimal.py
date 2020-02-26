def isNumber(s):
    if s == '' or s == ' ':
        return False
    l1 = [x for x in s]
    l2 = []
    d ={}

    for x in l1:
        if x.isdigit() == True:
            l2.append(x)
        elif x == ' ':
            if len(l2) == 0:
                pass
            else:
                l2.append(x)
        elif x == '-' or x == '+':
            if l2 == []:
                d.update({x:1})
                l2.append(x)
            elif l2[len(l2)-1] == 'e':
                l2.append(x)
            elif len(l2)>0:
                return False
        elif x in d:
            return False
        elif x == '.' and 'e' in d:
            return False
        elif x == '.':
            d.update({x:1})
            l2.append(x)
        elif x == 'e':
            if l2 == []:
                return False
            if l2[len(l2)-1].isdigit() == False:
                if l2[len(l2)-1] == '.':
                    d.update({x:1})
                    l2.append(x)
                else:
                    return False
            else:
                d.update({x:1})
                l2.append(x)
        else:
            return False
    
    if l2 == []:
        return False
    def contains_space(l2):
        while True:
            if l2[len(l2)-1] == ' ':
                l2.pop()
            else:
                break
        if ' ' in l2:
            return False
        else:
            return True
    
    def contains_digit(l2):    
        check = False
        for j in l2:
            if j.isdigit():
                return True
        return check
        
    if contains_digit(l2) == False:
        return False
    elif contains_space(l2) == False:
        return False
    elif l2[len(l2)-1] == 'e' or l2[len(l2)-1] == '+' or l2[len(l2)-1] == '-':
        return False
    elif s[0:2] == '.e':
        return False
    else:
        return True

if __name__ == "__main__":
    print(isNumber("0")," => true")
    print(isNumber(" 0.1 "), "=> true")
    print(isNumber("abc"), " => false")
    print(isNumber("1 a"), " => false")
    print(isNumber("2e10"), " => true")
    print(isNumber(" -90e3"), " => true")
    print(isNumber(" 1e"), " => false")
    print(isNumber("e3"), " => false")
    print(isNumber(" 6e-1"), " => true")
    print(isNumber(" 99e2.5"), " => false") #
    print(isNumber("53.5e93"), " => true")
    print(isNumber(" --6 "), " => false") #
    print(isNumber("-+3"), " => false") #
    print(isNumber("95a54e53"), " => false")
    print(isNumber("9."), " => true")