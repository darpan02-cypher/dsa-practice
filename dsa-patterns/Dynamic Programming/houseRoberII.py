from typing import List

class Solution:

#standard solution using helper function to handle the linear case of the house robber problem--

    '''
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
    '''


# my solution 

    def rob(self, nums: List[int]) -> int:
        # 1. Move bse cases to top
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])

        # scenerio 1- rob first house and skip last house
        dp1 = [0] * len(nums)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            dp1[i] = max(dp1[i - 1], nums[i] + dp1[i - 2]) # same house robber logic as in house robber I problem

        result1 = dp1[len(nums) - 2] # last house is skipped

        # scenerio 2- skip first house and rob last house
        dp2 = [0] * len(nums)
        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            dp2[i] = max(dp2[i - 1], nums[i] + dp2[i - 2]) # same house robber logic as in house robber I problem
        result2 = dp2[len(nums) - 1] # first house is skipped

        return max(result1, result2) # return the maximum of the two scenarios
    
# Example usage:
solution = Solution()
print(solution.rob([2, 3, 2]))  # Output: 3
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1, 2, 3]))  # Output:       4
