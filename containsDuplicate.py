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
