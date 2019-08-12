def mergeSort(a1, a2):
    x=0
    y=0
    sort = []
    while x<len(a1) or y<len(a2):
        if x == len(a1):
            sort.append(a2[y])
            y+=1

        elif y == len(a2):
            sort.append(a1[x])
            x+=1

        elif a1[x] < a2[y]:
            sort.append(a1[x])
            x+=1

        else:
            sort.append(a2[y])
            y+=1
    return sort

if __name__ == "__main__":
    
    l1 = [1,3,4,10]
    l2 = [1,2,5,6,11,12]
    print(mergeSort(l1,l2))