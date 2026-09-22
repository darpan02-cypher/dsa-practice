def binarySearch(nums: list, target: int):
    left, right = 0, len(nums)-1

    

    if len(nums) ==0: return "List is empty"

    while left<=right :
        middle = (left + right) // 2
        if nums[middle] ==target:
            return middle
        elif nums[middle] <target:
            left = left +1
        else:
            right =right -1
        
    return -1 # target not found #edge cases 
    #return "Target not found"

# Example usage: using all type of test cases
print(binarySearch([1, 2, 3, 4, 5], 3))  # Output: 2
print(binarySearch([1, 2, 3, 4, 5], 6))  # Output: -1
print(binarySearch([], 1))  # Output: "List is empty"
print(binarySearch([1, 2, 3, 4, 5], 1))  # Output: 0
print(binarySearch([1, 2, 3, 4, 5], 5))  # Output: 4    