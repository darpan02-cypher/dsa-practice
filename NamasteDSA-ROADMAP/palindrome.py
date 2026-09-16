def palindrom(x:int) -> bool:
    digits =list(str(abs(x))) # convert the integer to a list of its digits as strings

                              ## or digits == list(reversed(digits))
    if digits ==digits[::-1]: # check if the list of digits is the same as its reverse
        return True
    else:
        return False

#example usage:
x = 121
print(f"Is {x} a palindrome? {palindrom(x)}")   
#check for edge cases as well
                               #--------Using Strinf Slciing is easier approac--------#
                        
def palindrom2(x:int) -> bool:
    if x<0: #handle negative numbers, as they are not palindromes
        return False
    s= str(abs(x))

    return s==s[::-1]

# Example usage:
x = 12121
result = palindrom2(x)
print(f"Is {x} a palindrome2? {result}")                   