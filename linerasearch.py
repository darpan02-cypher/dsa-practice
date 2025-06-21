
class Solution:
    def linearSearch(self, n, num, arr) -> int:   # here ->int : means the function returns an integer
        for i in range(n):
            # Check if the current element matches the number to be searched
            # If found, return the index
            if arr[i] == num:
                return i
        return -1


# Example usage of linearSearch function
#take user input 
n, num = map(int, input().split())

arr = list(map(int, input().split()))  #split by commas for input or we could have used space 

# Call the linearSearch function
solution = Solution()  # Create an instance of the Solution class
result = solution.linearSearch(n, num, arr)

#print the result using the function
if result != -1:
    print(result)  #f is for formatted string i.e. it allows us to include variables directly in the string
else:
    print("Number not found in the array.")

