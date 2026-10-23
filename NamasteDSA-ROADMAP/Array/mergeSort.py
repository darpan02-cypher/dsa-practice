#The goal: merge nums2 into nums1 in sorted order in-place.
#using two pointers approach
def mergeSort(nums1, nums2):
    #initialize pointers for nums1 and nums2
    p1 = len(nums1)-1
    p2 = len(nums2)-1
    k = len(nums1) + len(nums2) - 1  # Pointer for the end of merged array
    # Extend nums1 to accommodate nums2
    nums1.extend([0] * len(nums2))
    # Merge in reverse order
    while p2 >= 0: # this loop will run until all elements of nums2 are merged into nums1
        if p1 >= 0 and nums1[p1] > nums2[p2]: # if the current element in nums1 is greater than the current element in nums2
            nums1[k] = nums1[p1]
            p1 -= 1
        else:
            nums1[k] = nums2[p2]
            p2 -= 1
        k -= 1

# Example usage
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
mergeSort(nums1, nums2)
print(f"The merged sorted array is: {nums1}")  


#pseudocode to remeber it in easy way
#1. Initialize pointers p1, p2, and k for nums1, nums2
#2. Extend nums1 to accommodate nums2
#3. While p2 >= 0:
#   a. If p1 >= 0 and nums1[p1] > nums2[p2]:
#       i. Set nums1[k] = nums1[p1]