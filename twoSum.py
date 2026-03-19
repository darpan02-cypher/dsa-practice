from typing import List
######################## O(n) ---faster then below solution
#Optimal Approach → HashMap (that is dictionary in Python) as it allows us to check if the complement (target - current number) exists in O(1) time. We can iterate through the list once, storing each number and its index in the dictionary. For each number, we check if its complement is already in the dictionary. If it is, we have found our two numbers and can return their indices. This approach has a time complexity of O(n) and a space complexity of O(n) due to the dictionary storing the numbers and their indices.
'''
class Solution:
    def twoSum(self, nums, target):
        seen = {}  # number: index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]  # found the pair
            seen[num] = i  # remember this number
        return []  # not needed because the problem says a solution always exists

'''


################### O(n^2) ---brute force solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


#nums, target = map((input().split()),int)

input_data = input("Enter numbers as a space-separated list followed by the target: ")
nums, target = map(int, input_data.split(','))
solution = Solution()

result = solution.twoSum(nums, target)

print(result)






