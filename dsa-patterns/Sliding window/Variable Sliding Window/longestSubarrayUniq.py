from tokenize import String


def longestSubstringUniq(s: str):

    seen = set() # useing set to store seen elements as it avoids duplicate
    left =0
    ans=0


    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1


            seen.add(s[right])

            current_length= right-left+1 #Running maximum 
            ans =max(ans, current_length)
        return ans

# example usage
s = "abcabcbb"
result = longestSubstringUniq(s)
print(f"The length of the longest substring without repeating characters in '{s}' is: {result}") # o/p: The length of the longest substring without repeating characters in 'abcabcbb' is: 3

#Complexity - O(n) for both time and space:
# though we are using nested while loop, the inner while loop will run at most n times in total across all iterations of the outer for loop. This is because each character is added and removed from the set at most once. Therefore, the overall time complexity is O(n). The space complexity is also O(n) due to the storage of characters in the set.
# is the time complexity O(n) even because of lookup of set? Yes, the average time complexity for lookups in a set is O(1), which means that even with the lookup operation, the overall time complexity remains O(n).