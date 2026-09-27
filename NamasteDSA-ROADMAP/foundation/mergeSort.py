def mergeSort(nums):
    if len(nums) <=1:
        return nums

    
    left_arr = nums[:len(nums)//2]
    right_arr =nums[len(nums)//2:]

    mergeSort(left_arr)
    mergeSort(right_arr)

    i=j= 0 # pointers for left and right array
    result = [] # final sorted array

    while i<len(left_arr) and j<len(right_arr):
        middle = (left_arr[i] + right_arr[j]) // 2
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i=i+1
        else:
            result.append(right_arr[j])
            j=+1
        result.extend(left_arr[i:])   # this is for the remaining elements in left array
        result.extend(right_arr[j:])  # this is for the remaining elements in right array

    return result


#example - all types of test cases
if __name__ == "__main__":
    nums = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", nums)
    sorted_nums = mergeSort(nums)
    print("Sorted array:", sorted_nums)

    nums = [5, 2, 9, 1, 5, 6]
    print("\nOriginal array:", nums)
    sorted_nums = mergeSort(nums)
    print("Sorted array:", sorted_nums)

    nums = [12, 11, 13, 5, 6, 7]
    print("\nOriginal array:", nums)
    sorted_nums = mergeSort(nums)
    print("Sorted array:", sorted_nums)

    nums = []
    print("\nOriginal array:", nums)
    sorted_nums = mergeSort(nums)
    print("Sorted array:", sorted_nums)

    nums = [1]
    print("\nOriginal array:", nums)
    sorted_nums = mergeSort(nums)
    print("Sorted array:", sorted_nums)
    