#Count Subarrays of Size K with Sum = X

#Adds condition checking
#Fixed window

def sum_subarray_x(arr, k, x):
    window_sum = sum(arr[:k])  # here arr[:k] is the first window of size k
    count = 0  # Initialize count


    #slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]  # remove the first element of the previous window and add the next element in the current window
        #condition check
        if window_sum == x:
            count += 1
    return count

# Example usage
arr = [1, 2, 3, 4, 5, 6]
k = 3
x = 9
result = sum_subarray_x(arr, k, x)
print(f"The count of subarrays of size {k} with sum {x} is:{result}")
# Output: The count of subarrays of size 3 with sum 9 is: 1
