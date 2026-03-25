#Use when Constant lnth (required window size) is given and we have to find the max/min/avg of the window
#find subarrarys or substrings of a fixed length and do some operation on it

#eg- find the max sum of a subarray of size k in an array
def max_sum_subarray(arr ,k):
    window_sum = sum(arr[:k])  # here arr[:k] is the first window of size k
    max_sum=window_sum #or other rquired value like min or avg

    #slide the window 
    for i in range(k, len(arr)):
        window_sum=window_sum -arr[i-k] + arr[i]  # remove the first element of the previous window and add the next element in the current windo
        max_sum=max(max_sum, window_sum) #update the max sum if the current window sum is greater
    return max_sum

# Example usage
arr = [1, 2, 3, 4, 5, 6]
k = 3
result = max_sum_subarray(arr, k)
print(f"The maximum sum of a subarray of size {k} is: {result}")
# Output: The maximum sum of a subarray of size 3 is: 15 

#this is how it is working 
# Initial window sum: 1 + 2 + 3 = 6
# Slide the window:
#iteration 1: where i=3, window_sum=6 - 1 + 4 = 9, max_sum=9
#iteration 2: where i=4, window_sum=9 - 2 + 5 = 12, max_sum=12