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


#below is also correct solution without using the seen dictionary, as it is not necessary for this problem. The main logic is to keep track of the minimum price seen so far and calculate the potential profit at each step, updating the maximum profit accordingly.
'''
def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)

        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit

# Example usage
prices = [7, 2,4,8,10]
result = maxProfit(prices)
print(f"The maximum profit is: {result}")
# Output: The maximum profit is: 5

#this is how it goes in each iteration:
# Iteration 1: price = 7, min_price = 7, profit = 0, max_profit = 0
# Iteration 2: price = 2, min_price = 2, profit = 0, max_profit = 0
# Iteration 3: price = 4, min_price = 2, profit = 2, max_profit = 2
# Iteration 4: price = 8, min_price = 2, profit = 6, max_profit = 6
# Iteration 5: price = 10, min_price = 2, profit = 8, max_profit = 8    



'''