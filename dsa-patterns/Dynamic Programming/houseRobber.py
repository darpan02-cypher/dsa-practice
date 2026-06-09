from typing import List


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
print(solution.rob([5,1,2,10,6,2,7,9,3,1]))  # Output: 25 but expected output in leetcode is 27 ... so 
