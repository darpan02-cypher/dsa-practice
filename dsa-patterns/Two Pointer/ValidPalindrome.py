def isPalindrome(s:str) -> bool:

    clean_s = "" #introduce empty string to storenew cleaned string

    for char in s:
        if char.isalnum():
            clean_s = clean_s + char.lower() #append the lower case of the character to the cleaned string

    #the complexity of two pointer approach is better - time = O(n) and space = O(1) 
    left, right = 0, len(clean_s) - 1 #initialize two pointers with left at the start and right at the end of the cleaned string
    while left < right:
        if clean_s[left] != clean_s[right]: #if the characters at the two pointers are not equal, return False
            return False
        left += 1 #move the left pointer to the right
        right -= 1 #move the right pointer to the left

    return True #if the loop completes without returning False, return True

## Example usage:
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))  # Output: True

     # another way ...but its complexity is O(n) and space - O(n) 
  
    """
    if cleaned_s == cleaned_s[::-1]:
        return True
    else:
        return False
    
    
    """