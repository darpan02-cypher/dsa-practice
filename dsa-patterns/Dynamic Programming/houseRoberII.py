from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        # Space-optimized House Robber I helper
        def rob_linear(houses: List[int]) -> int:
            prev2, prev1 = 0, 0
            for house in houses:
                # prev1 becomes the new choice, old prev1 becomes prev2
                prev2, prev1 = prev1, max(prev1, house + prev2)
            return prev1
        
        # Split into the two circular scenarios
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
    
# Example usage:
solution = Solution()
print(solution.rob([2, 3, 2]))  # Output: 3
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1, 2, 3]))  # Output:       4