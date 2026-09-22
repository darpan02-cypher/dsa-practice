def smallestInArr(nums: list):
    smallest = float('inf')
    if len(nums) == 0: return None

    for num in nums:
       if num < smallest:
            smallest = num
    return smallest



# Example usage: using all type of test cases
print(smallestInArr([3, 1, 4, 1, 5, 9]))  # Output: 1
print(smallestInArr([-5, -1, -3, -4]))  # Output: -5
print(smallestInArr([10, 20, 30, 40]))  # Output: 10
print(smallestInArr([]))  # Output: None