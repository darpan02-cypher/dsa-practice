class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0] * (n+1) # Step 1- create a list of size n+1 to store the number of ways to climb to each step, initialized with 0 ,  here using (n+1) lenght becoz we want to include the nth step in our dp array, so we need an extra slot for it. If we only created a list of size n, we would only have indices from 0 to n-1, and we wouldn't be able to store the number of ways to climb to the nth step.
        dp[0]=1 # Step 2-define base case: there is one way to climb zero steps (do nothing)
        dp[1]=1 # define base case: there is one way to climb one step (take one step)

        for i in range(2, n+1): #approach - bottom-up tabulation as we are using an iterative approach to fill the dp array from the base cases up to n
            dp[i]= dp[i-1] + dp[i-2]; #Step 3- the transition does always remain the same? -

        return dp[i]; #Step 4-  or use return dp[n] since we want the number of ways to climb to the nth step

#dp approach - top-down memoization
#example usage
solution = Solution()
print(solution.climbStairs(5)) # should return 8

#Note - In DP, dp[i] usually answers the question: "What is the solution for a size of i?" > Because we want to know the solution for size n, and arrays start counting at 0, the array must have n + 1 elements.
    


