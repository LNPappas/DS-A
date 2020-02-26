def rotate(nums,k):
    k%=len(nums)
    nums[:-k], nums[-k:] = nums[-k:], nums[:-k]
    return nums

if __name__ == "__main__":
    print(rotate([1,2,3,4,5,6,7],3))
    print(rotate([1,2,3,4,5,6,7],-1))
