#1. prifix sum
#used when we need to find the sum of elements in a subarray

# First - Single Query - i.e. find the sum of elements in a subarray from index i to j

def find_subarray_sum(array, i, j):
    subarray_sum=0

    for i in range(i, j+1):  #j+1 to include the element at index j
        subarray_sum += array[i]

    return subarray_sum

# Example usage
array = [1, 2, 3, 4, 5]
i = 1  # Starting index
j = 3  # Ending index
result = find_subarray_sum(array, i, j)
print(f"Sum of elements from index {i} to {i+j-1} is: {result}")
# Output: Sum of elements from index 1 to 3 is: 9


# Second - Multiple Queries - i.e. find the sum of elements in a subarray from index i to j for multiple queries
def find_subarray_sum_multiple_queries(array, queries):
    prefix_sum = [0] * (len(array) + 1)  # Create a prefix sum array

    # Calculate prefix sums
    for i in range(1, len(array) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + array[i - 1]

    results = []
    for i, j in queries:
        subarray_sum = prefix_sum[j + 1] - prefix_sum[i]
        results.append(subarray_sum)

    return results

# Example usage
array = [1, 2, 3, 4, 5]
queries = [(1, 3), (0, 2), (2, 4)]  # List of queries as tuples (i, j)
result = find_subarray_sum_multiple_queries(array, queries)
print("Sum of elements for each query:")
for i, j in queries:
    print(f"Sum of elements from index {i} to {j} is: {result[queries.index((i, j))]}")
# Output:
# Sum of elements from index 1 to 3 is: 9
# Sum of elements from index 0 to 2 is: 6
# Sum of elements from index 2 to 4 is: 12

#explaination of multiple queries:
# 1. Create a prefix sum array to store cumulative sums of the original array.
# 2. For each query, calculate the sum of the subarray using the prefix sum array.
# 3. The prefix sum allows us to compute the sum of any subarray in constant time O(1) after an initial O(n) preprocessing step.
# This approach is efficient for multiple queries as it avoids recalculating sums for overlapping subarrays.
# This is a more efficient way to handle multiple queries for subarray sums.
# This approach is particularly useful when you have a large array and need to answer multiple queries about subarray sums efficiently.


