def index_of_sum(l,s):
    comp = {}
    for index,value in enumerate(l):
        if value in comp.keys():
            return [comp.get(value), index]
        else:
            comp.update({s-value:index})
    return [None]

if __name__ == "__main__":
    l1 = [2, 7, 11, 15]
    l2 = [10, 8, 4, 1]
    target = 9
    print(index_of_sum(l1,target))
    print(index_of_sum(l2,target))