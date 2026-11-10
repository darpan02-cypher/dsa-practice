def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num # XOR operation to find the single number   # result = result ^ num... 
        # XOR of a number with itself is 0, and XOR of a number with 0 is the number itself. So, all the duplicate numbers will cancel each other out, leaving only the single number.)
    return result
# Example usage of all type of test cases
nums1 = [2, 2, 1]
print(f"The single number is: {singleNumber(nums1)}")  # Output: 1
nums2 = [4, 1, 2, 1, 2]
print(f"The single number is: {singleNumber(nums2)}")  # Output: 4
nums3 = [1]
print(f"The single number is: {singleNumber(nums3)}")  # Output: 1