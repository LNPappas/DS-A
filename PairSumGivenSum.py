#brute force would be a nested loop with runtime O(n^2)

def pairSum(n=[], s=0):
    '''
    given an array & a sum this func will determine
    if there is a pair in the array that equals the sum
    and return True or False.
    Runtime = O(n)

    '''
    comp = {}
    for element in n:
        if comp.get(element): 
            return True
        else:
            comp.update({s-element:element})
    return False




a1 = [2,3,4,10]
a2 = [2,3,4,4]
a3 = [5,3,2]
s = 8
d = {3:5, 2:4}
print(pairSum(a1,s))
print(pairSum(a2,s))
print(pairSum(a3,s))
print(pairSum(a3)) #<-default s = 0
print(pairSum([0, 0, 2]))
#print(pairSum(s)) <- would take s as n (a list) and try to iterate. Have to try/except clause
#print(pairSum(d,s)) <- cannot iterate dict, again try/except

