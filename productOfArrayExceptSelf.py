#Use prefix + suffix products

from typing import List
class Solution:
    def productOfArrayxceptSelf(self, nums):
     res = [1] * len(nums) # Initialize result array with 1s so that we can multiply the products later

        # Calculate prefix products
     prefix_product = 1
     for i in range(len(nums)):
         res[i] = prefix_product  # Store the prefix product in the result array as we iterate
         prefix_product *= nums[i] #prefix_product = prefix_product * nums[i]

        # Calculate suffix products and multiply with prefix products
     suffix_product = 1
     for i in range(len(nums) - 1, -1, -1): # Iterate from the end to the start eg- for i in range(len(nums) , end=-1, step=-1):
         res[i] *= suffix_product # Multiply the current result with the suffix product
         #res[i] = res[i] * suffix_product
         suffix_product *= nums[i]   #suffix_product = suffix_product * nums[i]
     return res
# Example usage:
solution = Solution()
nums = [1, 2, 4, 6]
print(solution.productOfArrayxceptSelf(nums))  # Output: [48,24,12,8]   

    
       