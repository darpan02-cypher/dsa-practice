def containsDuplicate(nums)->bool:
    my_set =set(nums)

    if len(nums) != len(my_set):
        return True
    else:
        return False
    
# Test cases
print(containsDuplicate([1, 2, 3, 1]))  # Output
print(containsDuplicate([1, 2, 3, 4]))  # Output
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output
