#brute force would be a nested loop restuling in O(a1*a2) or O(n*m)

def same(a1, a2):
    '''
    boolean function determining if any given two arrays
    contain the same element. O(a1+a2) of O(n+m)
    '''
    test = {}
    for element in a1:
        test.update({str(element) : element})
    for e in a2:
        if str(e) == test.get(str(e)):
            return True
    return False

a1 = ['a','b,','c']
a2 = [1,2,3]
a3 = [4,'z',2.5,2.0,'c']
print(same(a1,a2))
print(same(a3,a2))
print(same(a1,a3))