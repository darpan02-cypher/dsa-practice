#for Sorted arrays, pair questions, remaining duplicates or merging
#Eg1- Palindrome

def is_palindrome(string):
    start = 0
    end =len(string)-1

    while start<end:
        if string[start]!=string[end]: # Check if characters at start and end positions are not equal
            return False
        start+=1
        end-=1
    return True


#usage 
string = "racecar"
print(is_palindrome(string))  # Output: True




