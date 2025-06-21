# your code goes here  #Accepted - all test passed
class Solution:
    def sumArray(self,N, arr) ->int :
        total = 0
        for i in range(N):
            total = total + arr[i]
        return total
    
# Example usage of sumArray function
#take user input 
N = int(input())   # exact no statement fror test case to pass #Remenber01
arr = list(map(int, input().split()))  #split by spaces for input

# Call the sumArray function
solution = Solution()  # Create an instance of the Solution class - this is necessary to access the method
# Ensure that the input array has the expected number of elements
result = solution.sumArray(N, arr)

# Print the result using the function
if result != 0:
    print(result)  #Remmber02 for test case to pass --no statement in output
else:
    print("The array is empty or the sum is zero.")
    