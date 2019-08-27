def bubble(data):
    count = len(data)
    while count > 0:
        for index, element in enumerate(data):
            if index < len(data)-1:
                if element > data[index+1]:
                    data[index], data[index+1] = data[index+1], data[index]
        count -=1
    return data                 

if __name__ == "__main__":
    l = [3,1,4,7,2,8,0]
    print(bubble(l))