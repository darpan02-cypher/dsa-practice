import time

# ==========================================
# 1. DIVIDE AND CONQUER (NAIVE RECURSION)
# ==========================================
def fib_divide_and_conquer(n: int) -> int:
    """
    Computes Fibonacci using naive recursion.
    Time Complexity: O(2^n) - Exponential
    Space Complexity: O(n) - Recursive call stack
    """
    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
        
    # Divide and conquer step
    return fib_divide_and_conquer(n - 1) + fib_divide_and_conquer(n - 2)


# ==========================================
# 2. DYNAMIC PROGRAMMING (BOTTOM-UP TABULATION)
# ==========================================
def fib_dynamic_programming(n: int) -> int:
    """
    Computes Fibonacci using bottom-up iteration and an array.
    Time Complexity: O(n) - Linear
    Space Complexity: O(n) - Array storage
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
        
    # Table initialization
    table = [0] * (n + 1)
    table[1] = 1
    
    # Fill the table iteratively
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
        
    return table[n]


# ==========================================
# BENCHMARK AND TEST EXECUTION
# ==========================================
if __name__ == "__main__":
    # Test value (Keep this below 40 for Divide & Conquer, or it will freeze)
    n = 35
    
    print(f"--- Computing the {n}th Fibonacci Number ---")
    
    # Run Dynamic Programming First (Fast)
    start_time = time.time()
    dp_result = fib_dynamic_programming(n)
    dp_duration = time.time() - start_time
    print(f"[DP Approach]  Result: {dp_result} | Time taken: {dp_duration:.6f} seconds")
    
    # Run Divide and Conquer (Slow)
    print("Running Divide & Conquer (this might take a few seconds)...")
    start_time = time.time()
    dc_result = fib_divide_and_conquer(n)
    dc_duration = time.time() - start_time
    print(f"[D&C Approach] Result: {dc_result} | Time taken: {dc_duration:.6f} seconds")
    
    # Performance ratio
    if dc_duration > 0:
        ratio = dc_duration / (dp_duration if dp_duration > 0 else 1e-9)
        print(f"\nDynamic Programming was roughly {ratio:,.0f} times faster!")


## Note: The Divide and Conquer approach will become impractical for n > 40 due to its exponential time complexity.