#Kadane's algo - DP- It is used to find the maximum sum of a contiguous subarray in an array of integers. 
# The algorithm works by iterating through the array and keeping track of the current sum of the subarray being considered. 
# If the current sum becomes negative, it is reset to zero, as a negative sum would not contribute to a maximum sum in future iterations. 
# The maximum sum is updated whenever a new maximum is found. 
#____________________________________________________
#It is an O(n) solution to the Maximum Subarray Problem

#Instead of checking all subarrays (O(n²)), it does this:

#“At every index, decide — should I extend the current subarray or start fresh?”

def max_subarray(arr):
    max_sum = float('-inf') # Initialize max_sum to the smallest possible value to handle cases where all elements are negative
    current_sum = 0

    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0: # If current_sum becomes negative, reset it to 0 - this is kadane's algorithm to find the maximum sum of a contiguous subarray
            current_sum = 0

    return max_sum

# Example usage:
arr = [-2,1,-3,4,-1,2,1,-5,4]
result = max_subarray(arr)
print("Maximum subarray sum is:", result)
