#sort the array and retun second last element in it

def secondLargest(nums):

    #this apprach has a time complexity of O(nlogn) due to sorting, but it is simple and easy to understand.
    unique_nums = list(set(nums))  # Remove duplicates first
    
    if len(unique_nums) < 2:       # Check unique count after removing duplicates
        return None                 #need atlast 2 elemnsts in the list to find second largest
        
    unique_nums.sort()             # Sort in ascending order
    return unique_nums[-2]         # Return second to last element

# Example usage:
nums = [3, 1, 4, 4, 5, 2]
result = secondLargest(nums)
if result is not None:
    print("The second largest number is:", result)
else:
    print("Not enough unique elements to determine the second largest number.")

    #Optimal approach with time complexity of O(n) and space complexity of O(1)
def secondLargestOptimal(nums):
    first = second = float('-inf')  # Initialize first and second to negative infinity

    for num in nums:
        if num > first:              # If current number is greater than first
            second = first           # Update second to be the old first
            first = num              # Update first to be the current number
        elif first > num > second:   # If current number is between first and second
            second = num             # Update second to be the current number

    return second if second != float('-inf') else None  # Return None if no second largest found

# Example usage:
nums = [3, 1, 4, 4, 5, 2]
result = secondLargestOptimal(nums)
if result is not None:
    print("The second largest number (optimal) is:", result)
else:
    print("Not enough unique elements to determine the second largest number (optimal).")
