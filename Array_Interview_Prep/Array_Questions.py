from random import randint

def missing(arr):
    '''
    find missing integer from sequential array
    returns missing int
    O(n)
    '''
    return sum(range(arr[0], arr[len(arr)-1]+1)) - sum(arr)


def duplicate(arr):
    '''
    find duplicate numbers in array
    returns array of duplicate numbers
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
            
def num_in_array(arr, num):
    '''
        returns boolean if num in array
        O(n)
    '''
    return num in arr

def find_large_and_small(arr):
    '''
        finds largest and smallest element in unsorted array
        returns arary [largest, smallest]
        0(n)
    '''
    return [max(arr), min(arr)]

def pairs(arr, num):
    '''
    find all pairs on integer array whose sum is equal to given number
    returns pairs in list
    O(n)
    '''
    d = {}
    p = []
    for value in arr:
        temp = num - value
        if value in d:
            p.append((value, temp))
        else:
            d.update({temp:value})
    return p

def remove_dup(arr):
    '''
    removes all duplicated from array
    returns array
    O(n)
    '''
    return list(set(arr))

def quickSort(arr, start, end):

    def partition(arr, start, end):
        #set the last element in the array as the pivot
        pivot = arr[end]
        # i is the index of the smallest element
        # subtract 1 because the first time we use i we add 1
        i = start 

        #loop through arr. if element < pivot, move to left, else move to right. 
        #Pivot will be in correct place at end of loop
        for j in range(start, end):
            # if current element <= pivot move it to before the original start
            if arr[j] <= pivot:
                # increment starting index
                i +=1
                # swaps "start" with value that is less then pivot. 
                arr[i], arr[j] == arr[j], arr[i]
              
        arr[i+1], arr[end] = arr[end], arr[i+1]
        return i+1


    if start < end:
        p = partition(arr, start, end)
        quickSort(arr, start, p-1) 
        quickSort(arr, p+1, end)

    return arr 





if __name__ == "__main__":
# Missing numbers
    r = randint(0,100)
    r2 = randint(24,44)
    arrMiss = [x for x in range(0,101)]
    arrMiss2 = [x for x in range(24, 45)]
    arrMiss.pop(r)
    arrMiss2.remove(r2)
    print("Random: ", r, "Missing ", missing(arrMiss))
    print("Random: ", r2, "Missing ", missing(arrMiss2), "\n")

# Duplicate numbers
    arrDup = [x for x in range(0,101)]
    r3 = randint(0,101)
    r4 = randint(5,32)
    arrDup.append(r)
    arrDup.append(r2)
    arrDup.append(r3)
    arrDup.append(r4)
    print("Duplicates: ", r, r2, r3, r4, " Missing: ", duplicate(arrDup), "\n")

# Number in Array
    print(f"Is {r} in array: ", num_in_array(arrMiss, r))
    print(f"Is {r2} in array: ", num_in_array(arrMiss2, r2))
    print(f"Is {r3} in array: ", num_in_array(arrMiss, r3), "\n")

# Largest and Smallest elements in array
    a1 = [3,7,2,0,1,29,35,1002,-1,6,83]
    a2 = [randint(0, 1000) for r in range(0,100)]
    print(find_large_and_small(a1))
    print(find_large_and_small(a2), "\n")

# Find pairs that sum to given number in array
    print(pairs(a1, 9))
    print(pairs(arrMiss, 60), "\n")

# remove all duplicates from array:
    dup = [1,2,4,3,5,1,6,7,23,87,3243,1,1,1,2,2,2,3,3,3,4,4,4,87]
    print(remove_dup(dup), "\n")

# quicksort
    qrrQ = [4,1,7,2,9,3,6,0,10,8,5]
    length = len(qrrQ)-1
    print(quickSort(qrrQ, 0, length), "\n")