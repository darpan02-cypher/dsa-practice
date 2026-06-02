class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0] * (n+1) #create a list of size n+1 to store the number of ways to climb to each step, initialized with 0 ,  here using (n+1) lenght becoz we want to include the nth step in our dp array, so we need an extra slot for it. If we only created a list of size n, we would only have indices from 0 to n-1, and we wouldn't be able to store the number of ways to climb to the nth step.
        dp[0]=1
        dp[1]=1

        for i in range(2, n+1):
            dp[i]= dp[i-1] + dp[i-2];

        return dp[i];

#dp approach - top-down memoization
#example usage
solution = Solution()
print(solution.climbStairs(5)) # should return 8

#Note - In DP, dp[i] usually answers the question: "What is the solution for a size of i?" > Because we want to know the solution for size n, and arrays start counting at 0, the array must have n + 1 elements.
    


