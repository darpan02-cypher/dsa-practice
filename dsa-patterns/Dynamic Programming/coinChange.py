from typing import List


def coinChange(coins, amount):
    #with bfs appproarch
    #just with list 
    dp = [float('inf')] * (amount + 1) #not [0] because we want to find the minimum number of coins for each amount from 1 to amount
    dp[0] = 0 #base case 

    for coin in coins: #
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)     # the minimum number of coins needed to make up the amount x is either the current value dp[x] or the value of dp[x - coin] + 1 (which means we are using one more coin of the current denomination).



    return dp[amount] if dp[amount] != float('inf') else -1 

# example usage
coins = [1, 2, 5]
amount = 11
result = coinChange(coins, amount)
print(result)  # Output: 3 (11 = 5 + 5 + 1) 

#Time complexity of above solution is O(n*m) where n is the amount and m is the number of coins.
'''
Pseudocode:
    
    1. Create a "Wallet" list from 0 to target_amount.
    2. Fill it with "Infinity" (because we don't know the answers yet).
    3. Set Wallet[0] = 0 (It takes exactly 0 coins to make $0).
    
    4. For each COIN you have:
           For every AMOUNT from that coin's value up to the target_amount:
               
               Current_Best = Wallet[AMOUNT]
               Using_This_Coin = Wallet[AMOUNT - COIN] + 1
               
               Wallet[AMOUNT] = Minimum of (Current_Best, Using_This_Coin)
               
    5. If Wallet[target_amount] is still Infinity, return -1 (Impossible!)
       Otherwise, return Wallet[target_amount]



'''

#mental model - To find the fewest coins to make $10 using a $2 coin, look at your wallet for $8 ($10 - 2$) and add 1 to that coin count. If that number is smaller than what you already have written down for $10, overwrite it!

#Video youtube - https://www.youtube.com/watch?v=NNcN5X1wsaw



#------------------------------DFS - Recuresion with memoization-----------------------------
def coinChange(self, coins: List[int], amount: int) -> int:

        def dfs(amount):
            if amount == 0:
                return 0

            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins