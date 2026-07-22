#brute force approach 
#time complexity - O(n^2) as we. have to check all the subarrays possible and calculate their product
def maxProduct(nums):

    if len(nums) == 0:
        return False
    
    max_product = nums[0]  # Initialize max_product to the first element of the array

    for i in range(len(nums)):
        current_product = 1
        for j in range(i, len(nums)):
            current_product=current_product*nums[j]
            max_product=max(max_product, current_product)
        
    return max_product


#eg usage
nums = [2, 3, -2, 4]
result = maxProduct(nums)
print(result)  # Output: 6

#check for [-3, 0, -2]
nums = [-3, 0, -2]
result = maxProduct(nums)
print(result)  # Output: 0

nums= [0,2]
result = maxProduct(nums)
print(result)  # Output: 2
