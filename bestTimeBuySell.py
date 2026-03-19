from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #window_sum=sum(prices[:k])
        seen = {}
        profit =0
        min_price = prices[0] # Initialize min_price to the first price in the list

        for i, price in enumerate (prices):
            # Update min_price if the current price is lower than the previously recorded min_price 
            if price < min_price:
                min_price = price
            #else, calculate the potential profit by selling at the current price and buying at the min_price, and update the max profit if this potential profit is greater than the previously recorded max profit
            else:
                diff = price - min_price
                profit= max(profit, diff)

                seen[diff] = i # Store the index of the current price in the seen dictionary with the potential profit as the key

        return profit
    
# Example usage
prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
result = solution.maxProfit(prices)
print(f"The maximum profit is: {result}")
# Output: The maximum profit is: 5  