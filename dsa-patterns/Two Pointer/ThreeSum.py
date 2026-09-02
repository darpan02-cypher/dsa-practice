from typing import List


def threeSum(nums:List[int]):
    res = [] #set to store the triplets , using set to avoid duplicates
    nums.sort() #sort the array , as it will group the duplicates and also help in using two pointer approach

    for i in range(len(nums)-2): #iterate till len(nums)-2 as we need at least 3 elements to form a triplet
        if i > 0 and nums[i] == nums[i-1]: #skip the duplicates
            continue

        left, right = i+1, len(nums)-1 #two pointer approach
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0: #if sum is less than 0, move the left pointer to right to increase the sum
                left += 1
            elif total > 0: #if sum is greater than 0, move the right pointer to left to decrease the sum
                right -= 1
            else: #if sum is equal to 0, add the triplet to the result set and move both pointers to avoid duplicates
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]: #skip duplicates for left pointer
                    left += 1
                while left < right and nums[right] == nums[right-1]: #skip duplicates for right pointer
                    right -= 1
                left += 1
                right -= 1
    return res

#example usage
nums = [-1, 0, 1, 2, -1, -4]
result = threeSum(nums)
print(result)  # Output: [[-1, -1, 2], [-1, 0, 1]]