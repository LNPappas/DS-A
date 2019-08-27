def selection(array):
    i = 0
    while i < len(array)-1:
        for index, element in enumerate(array):
            if index == i:
                small = array[i]            
            if element < small:
                small = element
        array.remove(small)
        array.insert(i, small)
        i+=1
    return array

if __name__ == "__main__":
    l = [3,1,4,7,2,8,0]
    print(selection(l))
