from random import randint

def missing(arr):
    '''
    find missing integer from sequential array
    O(n)
    '''
    return sum(range(arr[0], arr[len(arr)-1]+1)) - sum(arr)


def duplicate(arr):
    '''
    find duplicate numbers in array
    O(n)
    '''
    d = {}
    for x in arr:
        if x not in d:
            d.update({x:1})
        else:
            d[x] +=1
    
    final = []
    for key, value in d.items():
        if value > 1:
            final.append(key)
    return final
            



if __name__ == "__main__":
# Missing numbers
    r = randint(0,100)
    r2 = randint(24,44)
    arrMiss = [x for x in range(0,101)]
    arrMiss2 = [x for x in range(24, 45)]
    arrMiss.pop(r)
    arrMiss2.remove(r2)
    print("Random: ", r, "Missing ", missing(arrMiss))
    print("Random: ", r2, "Missing ", missing(arrMiss2))

# Duplicate numbers
    arrDup = [x for x in range(0,101)]
    r3 = randint(0,101)
    r4 = randint(5,32)
    arrDup.append(r)
    arrDup.append(r2)
    arrDup.append(r3)
    arrDup.append(r4)
    print("Duplicates: ", r, r2, r3, r4, " Missing: ", duplicate(arrDup))
