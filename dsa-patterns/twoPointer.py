#for Sorted arrays, pair questions, remaining duplicates or merging
#Eg1- Palindrome

def is_palindrome(string):
    start = 0
    end =len(string)-1

    while start<end:
        if string[start]!=string[end]:
            return False
        start+=1
        end-=1
    return True


#usage 
string = "racecar"
print(is_palindrome(string))  # Output: True




