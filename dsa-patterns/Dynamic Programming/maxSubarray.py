from typing import List


def maxSubarray(nums:List[int]) -> int:

    dp= [0]* len(nums) # Initialize the dp array with zeros
    max_sum = nums[0]

    for i in range(0, len(nums)):
        if i == 0:
            dp[i] = nums[i] # Base case: the maximum sum at index 0 is just the first element
        else:
            max_sum = max(nums[i], max_sum +  nums[i])
            dp[i] = max_sum # Update the dp array with the maximum sum at each index
    return max(dp) # Return the maximum sum from the dp array

# Example usage:
arr = [-2,1,-3,4,-1,2,1,-5,4]
result = maxSubarray(arr)
print("Maximum subarray sum is:", result) # Output: 6 (subarray [4,-1,2,1] has the largest sum)

#and also check other edge case
arr2= [-1]
result2 = maxSubarray(arr2)
print("Maximum subarray sum is:", result2) # Output: -1 (subarray [-1] has the largest sum)


#======================
'''This is another implementation of the same problem using a slightly different approach.
 It also uses dynamic programming to keep track of the maximum sum at each index, but it does not use an additional dp array to store the maximum sums. 
 Instead, it updates the current maximum sum directly and keeps track of the overall maximum sum found so far. Both implementations have a time complexity of O(n) and a space complexity of O(n) for the first implementation (due to the dp array) and O(1) for the second implementation (since it only uses a few variables).'''
'''
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        current_max = nums[0]
    
        for i in range(1, len(nums)):
        # Either start a new window at nums[i] or add it to current window
            current_max = max(nums[i], current_max + nums[i])
            max_so_far = max(max_so_far, current_max)
        
        return max_so_far
'''