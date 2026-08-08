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

            current_length= right-left+1
            ans =max(ans, current_length)
        return ans

# example usage
s = "abcabcbb"
result = longestSubstringUniq(s)
print(f"The length of the longest substring without repeating characters in '{s}' is: {result}") # o/p: The length of the longest substring without repeating characters in 'abcabcbb' is: 3

