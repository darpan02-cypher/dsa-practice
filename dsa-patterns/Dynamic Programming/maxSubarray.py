from typing import List


def maxSubarray(nums:List[int]) -> int:

    dp= [0]* len(nums) # Initialize the dp array with zeros
    max_sum = nums[0]

    for i in range(1, len(nums)):
        max_sum = max(nums[i], max_sum +  nums[i])
        dp[i] = max_sum # Update the dp array with the maximum sum at each index
    return max(dp) # Return the maximum sum from the dp array

# Example usage:
arr = [-2,1,-3,4,-1,2,1,-5,4]
result = maxSubarray(arr)
print("Maximum subarray sum is:", result) # Output: 6 (subarray [4,-1,2,1] has the largest sum)

#======================

