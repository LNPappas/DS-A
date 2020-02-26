def longestPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    try:
        if strs == "":
            return ''
        smallest = min(strs)
        pref = ''

        i = 0
        while i < len(smallest):
            check = smallest[i]
            for word in strs:
                if word[i] != check:
                    return pref
            i +=1
            pref = pref + check
                
        return pref
                    
    except:
        return ''

if __name__ == "__main__":
    l = ['flowers', 'flow','flux', 'flake']
    print(longestPrefix(l))
    
