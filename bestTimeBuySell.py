from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #window_sum=sum(prices[:k])
        seen = {}
        profit =0
        min_price = prices[0]

        for i, price in enumerate (prices):
            #the index compared must be greater then the index of min_price becoz selling date can be only after buying date is the logic
            if price < min_price:
                min_price = price
            else:
                diff = price - min_price
                profit= max(profit, diff)

                seen[diff] = i

        return profit
    
# Example usage
prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
result = solution.maxProfit(prices)
print(f"The maximum profit is: {result}")
# Output: The maximum profit is: 5  