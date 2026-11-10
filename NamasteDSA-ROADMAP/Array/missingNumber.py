def missingNumber(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum   

# Example usage of all type of test cases
nums1 = [3, 0, 1]
print(f"The missing number is: {missingNumber(nums1)}")  # Output: 2
#time complexity is O(n) and space complexity is O(1)
#----------------------------------------------------------------
def missingNumber2(nums):
    nums.sort() #sort the array first

    #handle the edge case first , i.e 0
    if nums[0] != 0:
        return 0
    
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums) # this is the case when all numbers are present in the array, so the missing number is n i.e the length of the array
#time complexity is O(nlogn) and space complexity is O(1)
