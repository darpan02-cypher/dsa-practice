from typing import List


def TwoIntSumII(nums:List[int], target):

    l, r= 0, len(nums)-1

    while l<r:
        compli = target-nums[l]

        if nums[r]==compli:
            return [l+1, r+1]
        elif nums[r] > compli:
            r=r-1
        else:
            l=l+1

#example usage

numbers1 = [2, 7, 11, 15]
target1 = 9
print("Example 1 Output:", TwoIntSumII(numbers1, target1))  # Output: [1, 2]

# Example 3: Duplicate values
numbers3 = [2, 3, 4]
target3 = 6
print("Example 3 Output:", TwoIntSumII(numbers3, target3))  # Output: [1, 3]
