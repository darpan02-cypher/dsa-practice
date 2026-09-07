def trap_rain_water(height):
    if not height:
        return 0

    l, r = 0 , len(height) - 1

    leftMax, rightMax = height[l] ,height[r]
    res = 0 # total trapped water accumulated

    while l<r:
        if leftMax < rightMax: #In the two-pointer approach, always move the pointer on the side with the smaller max height.
            l+=1
            leftMax=max(leftMax, height[l])
            res = res + (leftMax - height[l])
        else:
            r-=1
            rightMax=max(rightMax, height[r])
            res = res + (rightMax - height[r])
    return res

#example
height=[0,2,0,3,1,0,1,3,2,1]
print(trap_rain_water(height)) # Output: 9


#easier short pseudocode to remeber:
# 1. Initialize two pointers at the start and end of the array
# 2. Keep track of the maximum height seen so far from both sides
# 3. Move the pointer on the side with the smaller max height
# 4. Add the difference between the current height and the max height to the result
# 5. Continue until the pointers meet