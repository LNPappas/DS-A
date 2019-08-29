def insertion(array):
    for i in range(1, len(array)): 
        temp = array[i] 
        j = i-1
        while j >=0 and temp < array[j] : 
                array[j+1] = array[j] 
                j -= 1
        array[j+1] = temp 
    return array

if __name__ == "__main__":
    l = [3,1,4,7,2,8,1]
    print(insertion(l))