from random import randint
def bestRotation(A):
    N = len(A)
    bad = [0] * N
    for i, x in enumerate(A):
        left, right = (i - x + 1) % N, (i + 1) % N
        bad[left] -= 1
        bad[right] += 1
        if left > right:
            bad[0] -= 1

    best = -N
    ans = cur = 0
    for i, score in enumerate(bad):
        cur += score
        if cur > best:
            best = cur
            ans = i
    return ans

if __name__ == "__main__":
    l = []

    while i < 10:
        for x in range (0,9):
            l.append(x)
            i+=1