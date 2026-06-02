
'''
def fib(n):
    if n <= 0:
        return 0. #base cases - you have to handle 
    elif n == 1:
        return 1. #base cases
    else:
        return fib(n - 1) + fib(n - 2)
    
'''
'''
#dp approach - top-down memoizatio

#step 1 - create a memoization dictionary to store previously computed values
    memo = {}  
def fib(n):

   

    

    #step 2 - base cases
    if n <= 0:
        return 0 ;
    elif n == 1:
        return 1 ;
    #step 3 - check if the value is already computed
    if n in memo:
        return memo[n]
    #step 4 - compute the value recursively and store it in the dp variable
    memo[n] = fib(n - 1) + fib(n - 2) #memo[] 
    return memo[n]

#example usage
print(fib(10)) # should return 55
 '''

#dp- Bottom-up tabulation approach

def fib(n):
   #step 1 - create a table to store the Fibonacci values up to n -- we can alos use two variables to store the last two Fibonacci numbers instead of an array or dictionary
    memo = [0] * (n + 1)  # "create a list containing n + 1 elements, where every single element is initialized to the number 0."
    memo[1] = 1  # Base case: F(1) = 1
    
        # Guard clauses for edge cases
    if n <= 0: 
        return 0
    #step 2 - fill the table iteratively
    for i in range (2, n+1):
        memo[i] = memo[i-1] + memo[i-2]   
    return memo[n]  # Return the nth Fibonacci number
#example usage
print(fib(10)) # should return 55


'''

# used memo as dict in botom up approach
def fib(n):
    memo = {0: 0, 1: 1}  # Base cases
    
    if n in memo:
        return memo[n]
    
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    
    return memo[n]
'''