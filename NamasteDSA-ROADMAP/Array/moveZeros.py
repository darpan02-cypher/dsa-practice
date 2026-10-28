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

#easy to remeber pseudo code
# 1. Initialize a pointer x to 0.
# 2. Iterate through the array with index i.
# 3. If the current element nums[i] is not zero, assign it to nums[x] and increment x.
# 4. After the loop, fill the remaining positions in the array with zeros from index x to the end of the array.
