#in place without coping the array
def moveZeros(nums):
    x=0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[x] = nums[i]
            x = x+1
    for i in range(x, len(nums)):
        nums[i] = 0

# Example usage of all type of test cases
nums1 = [0, 1, 0, 3, 12]
moveZeros(nums1)
print(f"The array after moving zeros is: {nums1}")  # Output: [1, 3, 12, 0, 0]  

