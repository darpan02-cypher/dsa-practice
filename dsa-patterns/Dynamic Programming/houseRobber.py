from typing import List

'''This solution is not correct as it does not consider the case where we can skip a house to maximize the amount robbed. The correct approach is to use dynamic programming to keep track of the maximum amount that can be robbed up to each house, considering both the case of robbing the current house and skipping it. Here is the corrected code:
class Solution:
    def rob(self, nums: List[int]) -> int:
        sum_odd=0 #odd positions sum
        sum_even=0 # even position sum
        dp_max= 0

        for i in range (0, len(nums)):
            if i%2==0: #even position
                sum_even = nums[i] + sum_even
            else: #odd position
                sum_odd = nums[i] + sum_odd
            
            dp_max = max(sum_even, sum_odd)
        return dp_max;

# Example usage:
solution = Solution()
print(solution.rob([1, 2, 3, 1]))  # Output:

#test cases
print(solution.rob([2, 7, 9, 3, 1]))  # Output: 12
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1, 2, 3]))  # Output: 4
#[5,1,2,10,6,2,7,9,3,1]
print(solution.rob([5,1,2,10,6,2,7,9,3,1]))  # Output: 25 but expected output in leetcode is 27 ... so this approach is not correct as it is not considering the case where we can skip
''' 

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Handle edge cases where the input list is empty or has only one house
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Create a dp array to store the maximum amount that can be robbed up to each house
        dp = [0] * len(nums) # Initialize the dp array with zeros
        dp[0] = nums[0] 
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            # For each house, decide whether to rob it (and add its value to the maximum from two houses back)
            # or skip it (and take the maximum from the previous house)
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1] # -1 as we want the last element which contains the maximum amount that can be robbed from all houses ,,,,, can we use dp[i] here? - no we cannot use dp[i] here because we are outside the loop and dp[i] would be out of bounds, we need to return the last element of the dp array which is dp[-1] or dp[len(nums)-1] both are correct.