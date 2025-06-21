from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):   # Iterate through the list
            # Compare the current element with all subsequent elements
            # This is a brute force approach and has O(n^2) time complexity
            for j in range(i + 1, len(nums)):  #
                if nums[i] == nums[j]:
                    return True
        return False


#arr = list(map(int, input("Enter numbers separated by space: ").split()))
#print("Enter youir array", arr)

arr= [1, 2, 3, 3,4]
# hasDuplicate()  # Removed as it is not defined outside the Solution class
solution = Solution()
print(solution.hasDuplicate(arr))