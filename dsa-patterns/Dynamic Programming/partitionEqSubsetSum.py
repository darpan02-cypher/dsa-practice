from typing import List


def partitionEqSubsetSum(nums: List[int]) -> bool:

    
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    

    # Create a DP array to store whether a subset sum is possible
    dp = [False] * (target + 1) #Create a boolean list of size target + 1 (indices 0 to 11) initialized to False. This keeps track of which sums are possible to achieve.
    dp[0] = True  # A subset sum of 0 is always possible

    for num in nums:
        # Traverse the dp array backwards to avoid using the same number multiple times
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]

# Example usage:
nums = [1, 5, 11, 5]
result = partitionEqSubsetSum(nums)
print(result)  # Output: True


#easier seodocode to remember lifetime
# Initialize a DP array to track possible subset sums
# dp = [False] * (target + 1)
# Set dp[0] to True since a subset sum of 0 is always possible
# For each number in the input list:
#     For each possible sum from target down to the current number:
#         Update dp[j] to True if dp[j - num] is True
# Return dp[target] to check if a subset sum equal to target is possible
