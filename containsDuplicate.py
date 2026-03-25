def containsDuplicate(nums)->bool:
    #seen = {} #if trying with dictionary then it will store both key andvalue
        my_set=set(nums) #withset it will only store unique element and search complexity -O(1) , while list search complexity is O(n)


        if len(nums)!=len(my_set): #if lenght of both not same then there is a duplicate existing in list
            return True

        else:
            return False # if the lenght is same then there isn't any duplicate 
    
# Test cases
print(containsDuplicate([1, 2, 3, 1]))  # Output
print(containsDuplicate([1, 2, 3, 4]))  # Output
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output

#pseaudo code
#step 1- create a set from the input list, which will store only unique elements
#step 2- compare the length of the original list with the length of the set
#step 3- if the lengths are different, it means there are duplicates in the original list, so return True
#step 4- if the lengths are the same, it means there are no duplicates in the original list, so return False

#--------O(n) using a set to track seen numbers
def containsDuplicate(nums) -> bool:
    seen = set()  # Create an empty set to track seen numbers

    for num in nums:  # Iterate through each number in the input list
        if num in seen:  # Check if the number is already in the seen set
            return True  # If it is, we have a duplicate, so return True
        seen.add(num)  # Otherwise, add the number to the seen set

    return False  # If we finish iterating without finding duplicates, return False