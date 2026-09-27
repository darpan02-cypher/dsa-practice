def removeDuplicate(nums: list[int]) -> int:
    if not nums:
        return 0

    # Initialize a pointer for the position of the next unique element
    unique_pos = 1

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the previous one, it's unique
        if nums[i] != nums[i - 1]:
            nums[unique_pos] = nums[i]# here we assign 
            unique_pos += 1
        else:
            # If the current element is the same as the previous one, it's a duplicate
            continue #no need of else ..just written for clarity

    return unique_pos

#time and space complexity for this is - O(n) and O(1)

# Example usage
test_cases = [
    [1, 1, 2],
    [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
    [],
    [1],
    [1, 2, 3, 4, 5],
]
for nums in test_cases:
    length = removeDuplicate(nums)
    print(f"After removing duplicates: {nums[:length]}, New length: {length}")     


#easy to remember approach:
#1. Initialize a pointer for the position of the next unique element (unique_pos) to 1.
#2. Iterate through the array starting from the second element (index 1).
#3. For each element, compare it with the previous element.
#4. If the current element is different from the previous one, it is unique. Move it to the position indicated by unique_pos and increment unique_pos.
#5. Continue this process until the end of the array is reached.
#6. Return unique_pos, which represents the length of the array with unique elements. The first unique_pos elements of the array will contain the unique elements in their original order. 
    
