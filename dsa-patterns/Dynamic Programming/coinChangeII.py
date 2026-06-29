from typing import List

# this line in problem "You may assume that you have an unlimited number of each coin and that each value in coins is unique." gives hint that this is UNBOUNDED KNAPSACK

def coinChangeII(amount, coins:List[int]) -> int:
    cache={} # hashmap to store

    def dfs(i,a):
        if a==amount: return 1 #base case
        if a>amount: return 0 #
        if i==len(coins): return 0 # this is out of bound
        if (i,a) in cache : return cache[(i, a)] #if we alrady have computed

        cache[(i,a)] = dfs (i, a + coins[i]) + dfs(i+1 , a) # dfs(i+1,a) - this case is when we skip the coin by increaing the index by 1
        return cache[(i, a)]
    
    return dfs(0,0)

#example use case 

# Test case 1: Standard case
# Amount = 5, Coins = [1, 2, 5]
# Combinations: [1,1,1,1,1], [1,1,1,2], [1,2,2], [5] -> Expected Output: 4
amount1 = 5
coins1 = [1, 2, 5]
result1 = coinChangeII(amount1, coins1)
print(f"Combinations for amount {amount1} with coins {coins1}: {result1}")

# Test case 3: Amount is 0 (1 way to make 0: choosing no coins)
# Amount = 0, Coins = [1, 2, 3] -> Expected Output: 1
amount3 = 0
coins3 = [1, 2, 3]
result3 = coinChangeII(amount3, coins3)
print(f"Combinations for amount {amount3} with coins {coins3}: {result3}")

# Test case 2: No possible combinations
# Amount = 3, Coins = [2] -> Expected Output: 0
amount2 = 3
coins2 = [2]
result2 = coinChangeII(amount2, coins2)
print(f"Combinations for amount {amount2} with coins {coins2}: {result2}")