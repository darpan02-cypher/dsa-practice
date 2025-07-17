from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n # Initialize result array with 1s so that we can multiply the products later

        # Calculate left products
        left_product = 1
        for i in range(n):
            result[i] = left_product  # Store the left product in the result array as we iterate
            left_product *= nums[i] #left_product = left_product * nums[i]

        # Calculate right products and multiply with left products
        right_product = 1
        for i in range(n - 1, -1, -1):   # Iterate from the end to the start eg- for i in range(len(nums) , end=-1, step=-1):
            result[i] *= right_product # Multiply the current result with the right product
            #result[i] = result[i] * right_product
            right_product *= nums[i]   #right_product = right_product * nums[i]

        return result

# Example usage:
solution = Solution()
nums = [1, 2, 4, 6]
print(solution.productExceptSelf(nums))  # Output: [48,24,12,8]


#simple explanation:
# The function calculates the product of all elements in the list except the current element for each position.
# It does this by first calculating the product of all elements to the left of each position, and then multiplying it with the product of all elements to the right of that position.


