def max_sub(l):
    largest_end = best_start = start = end = best = 0
    for index, value in enumerate(l):
        largest_end += value
        best = max(largest_end, best)
        if largest_end <= 0:
            start = index+1
            largest_end = 0
        elif largest_end == best:
            best_start = start
            end = index+1
    b = best_start
    l1 = []
    while b < end:
        l1.append(l[b])
        b+=1
    return l1, best

if __name__ == "__main__":
    m, s = max_sub([-2,1,-3,4,-1,2,1,-5,4])
    print("The Sub Array with the maximum value is:", m)
    print("With a sum of: ", s)

