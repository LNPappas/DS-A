def maxArea(height):
    '''
        given array containing list of heights of pillars
        find maxArea available to fill with water
        O(n)
    '''
    # set left pointer and result to zero
    left = result = 0
    # set right pointer and width to the end of the array
    right = width = len(height)-1
    # reverse iterate through length of array
    for w in range(width, 0, -1):
        # we want the height from the lower pillar because all the water above it will drain over it
        # if height at left pointer < height at right pointer
        if height[left] < height[right]:
            # set result to higher area
            # area = height[left]*w
            result = max(result, height[left]*w)
            # increase the left pointer
            left += 1
        # else the height at the right pointer is lower
        else:
            # set result to higher hight
            result = max(result, height[right]*w)
            right -=1
    # return greatest area
    return result


if __name__ == "__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7]))