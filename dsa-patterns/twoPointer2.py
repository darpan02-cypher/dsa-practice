#for Sorted arrays, pair questions, remaining duplicates or merging

#pair sum in sorted array using two pointer approach

def pair_sum(arr, target):
    left, right= 0, len(arr)-1 # initialize two pointers

    while left<right:
        if arr[left]+arr[right]==target:
            return (left, right)
        elif arr[left]+arr[right]<target:
            left+=1 #move left pointer right to increase the sum
        else:
            right-=1 #move right pointer left to decrease the sum
    return None
    

#usage
arr = [1, 2, 3, 4, 6]
target = 6
result = pair_sum(arr, target)
print(result)  # Output: (1, 3)
