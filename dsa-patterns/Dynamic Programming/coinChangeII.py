from typing import List

# this line in problem "You may assume that you have an unlimited number of each coin and that each value in coins is unique." gives hint that this is UNBOUNDED KNAPSACK

def coinChangeII(amount, coins:List[int]) -> int:
    cache={} # hashmap to store 



