def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if str == '':
        return ''

    i = 0
    d = {}
    highest_value = 0
    for index, value in enumerate(strs):
        if value[i] not in d:
            l = [strs[index]]
            d.update({value[i]:l})
        else:
            l = d.get(value[i])
            l.append(strs[index])
            if len(l) > highest_value:
                highest_value = len(l)
            d.update({value[i]:l})

    
    highest = 0
    pref = ''
    for key, value in d.items():
        i = 0
        j = 0
        k = 1
        while i < len(value)-1:
            while i+k < len(value): 
                if j < len(value[i]) and j < len(value[i+k]):
                    if value[i][j] == value[i+k][j]:
                        j+=1

                        if j >= highest:
                            highest = j
                            pref = value[i][:j]
                            
                    else:
                        k +=1
                        j = 0
                else:
                    k +=1
                    j = 0
                    
            i+=1
            k = 1
            j = 0

    return pref
if __name__ == "__main__":
    l = ['abc', 'flowers', 'cook', 'flow', 'cookies', 'abcdefg', 'flux', 'abcdefghi']
    print(longestCommonPrefix(l))
