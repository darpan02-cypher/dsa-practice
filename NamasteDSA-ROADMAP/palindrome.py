def palindrom3(x:int) -> bool:
    #using math fucnction - Asked in Interviews 
     
    if x == 0:
        return True  # Zero is a palindrome
    digits_arr = []
    num = abs(x)    # Get the absolute value of the number to handle negative numbers

    if num == 0:
        digits_arr.append(0)
    else:
        while num > 0:
            digits_arr.append(num % 10)  # Extract the last digit
            num = num // 10               # Remove the last digit from the number
    # Check if the list of digits is the same as its reverse
    return digits_arr == digits_arr[::-1]

#example usage:
x = 12321
result = palindrom3(x)
print(f"Is {x} a palindrome3? {result}")







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
                               #--------Using String Sliciing is easier approac--------#
                        
def palindrom2(x:int) -> bool:
    if x<0: #handle negative numbers, as they are not palindromes
        return False
    s= str(abs(x))

    return s==s[::-1]

# Example usage:
x = 12121
result = palindrom2(x)
print(f"Is {x} a palindrome2? {result}")    


