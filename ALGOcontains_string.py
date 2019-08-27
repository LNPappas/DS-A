def contain_str(s1, s2, s3):
    '''
    function determines if all elements of third string contained in previous two
    '''
    st = s1 + s2
    d1 = {}
    d2 = {}
    i = 0
    j=0
    while i < len(st):
        if st[i] not in d1:
            d1.update({st[i]:1})
        else:
            d1.update({st[i]:d1.get(st[i])+1})
        i+=1
    while j < len(s3):
        if s3[j] not in d2:
            d2.update({s3[j]:1})
        else:
            d2.update({s3[j]:d2.get(s3[j])+1})
        j+=1

    for key, value in d2.items():
        if d1.get(key) < value or d1.get(key == False):
            return False
    return True

if __name__ == "__main__":
    s1 = 'abcd'
    s2 = 'abcd'
    s3 = 'acddd'
    print(inter_str(s1,s2,s3))