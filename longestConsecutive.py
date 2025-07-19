from typing import List

#O(n^2) solution
"""
1.Pick a no from list (nums)
2. Keep it in Temp[] array as seen no
3.Comparenewly picked from nums & compare with other as nums[i]=num[j]+1 or num[i]==num[j]-1
4.If this no. matches &not in tem[] , then append it to temp[]
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j]-1:
                    temp.append(nums[i])
        return len(temp)

# Example usage:
solution = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(solution.longestConsecutive(nums))  # Output: 4 (the longest consecutive sequence is [1, 2, 3, 4])











