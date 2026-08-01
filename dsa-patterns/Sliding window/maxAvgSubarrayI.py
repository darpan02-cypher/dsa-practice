from git import List


def maxAvgSubarry(nums:List[int], k:int) -> float:
    n = len(nums) 
    if n < k: # If the length of the array is less than k, return 0.0 as we cannot form a subarray of size k
        return 0.0

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum / k

#Example usage
nums = [1, 12, -5, -6, 50, 3]
k = 4
result = maxAvgSubarry(nums, k)
print(f"The maximum average of subarrays of size {k} is: {result}") # Output: The maximum average of subarrays of size 4 is: 12.75
