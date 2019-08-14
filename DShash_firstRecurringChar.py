def recurr(array):
    table = {}
    for x in array:
        if x in table.keys():
            return x
        else:
            table.update({x:1})
    return 'No reccuring charaters'

if __name__ == "__main__":
    print(recurr([1,2,3,4,5,1]))
    print(recurr([1,2,3,2,4,5,1]))
    print(recurr([1,2,3,4,5]))
    print(recurr([0,0]))