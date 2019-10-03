def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    def search(a1,a2,m):
        l = []
        num1 = num2 = 0
        while num1 < len(a1) or num2 < len(a2):
            if num1 == len(a1):
                l.append(a2[num2])
                num2+=1
            elif num2 == len(a2):
                l.append(a1[num1])
                num1+=1                
            elif a1[num1] <= a2[num2]:
                l.append(a1[num1])
                num1+=1
            else:
                l.append(a2[num2])
                num2+=1

            if m < len(l):
                return l


    lenTotal = len(nums1) + len(nums2)
    if lenTotal == 2:
        return (nums1[0] + nums2[0])/2
    m = lenTotal//2
    m2 = 0
    if lenTotal%2 == 0:
        m2 = m-1

    l = search(nums1,nums2,m)

    if m2 != 0:
        return (l[m]+l[m2])/2
    else:
        return l[m]

    


if __name__ == "__main__":
    print(findMedianSortedArrays([1,3],[2])) #2
    print(findMedianSortedArrays([1,2],[3,4])) #2.5
    print(findMedianSortedArrays([1,3],[2,4]))
    print(findMedianSortedArrays([1],[2])) #1.5
    print(findMedianSortedArrays([2],[2])) #2