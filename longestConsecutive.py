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
        if not nums:
            return 0

        nums.sort()  # Sort the list to find consecutive numbers
        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            elif nums[i] == nums[i - 1] + 1:  # Check for consecutive numbers
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1  # Reset streak for new sequence

        return max(longest_streak, current_streak)  # Final check for the last streak







#O(n) solution
"""
1. If the input list 'nums' is empty:
    a. Return 0

2. Create a HashSet called 'num_set' from 'nums' to store unique numbers.

3. Initialize a variable 'longest_streak' to 0 to keep track of the longest sequence found.

4. For each number 'num' in 'num_set':
    a. If 'num - 1' is NOT in 'num_set':
        i. This means 'num' is the start of a new sequence.

        ii. Set 'current_num' to 'num' (the current number in the sequence).

        iii. Set 'current_streak' to 1 (we have found one number in the sequence).

        iv. While 'current_num + 1' is in 'num_set':
            - Increment 'current_num' by 1 (move to the next number).
            - Increment 'current_streak' by 1 (count this number in the sequence).

        v. Update 'longest_streak' to be the maximum of 'longest_streak' and 'current_streak'.

5. After checking all numbers, return 'longest_streak' as the result.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        longest_streak = 0
        for num in nums_set:
            if num-1 not in nums_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)
        return longest_streak


# Example usage:
solution = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(solution.longestConsecutive(nums))  # Output: 4 (the longest consecutive sequence is [1, 2, 3, 4])











