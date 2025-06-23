from typing import List
#Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Join the strings with a special character that won't appear in the strings
        # Step 1: Initialize an empty string to store the result
        result = ''
        # Step 2: Loop through each string in the list
        for s in strs:
            # Step 3: Add the string and a '#' separator to the result
            result += s + '#'
        # Step 4: Return the final encoded string
        return result

    def decode(self, decode_str: str) -> List[str]:
        # Split the string by the special character to get the original strings
        return decode_str.split('#')[:-1]


solution= Solution()
strs=["neet","code","love","you"]
#print(join_str)
print(solution.encode(strs))
print(solution.decode(solution.encode(strs)))


'''Goal:

Combine a list of strings into one string (encode)

Recover the exact original list from that string (decode)'''

#explaination of above code in steps-
# 1. The `encode` method takes a list of strings and joins them into a single string, appending a special character (`#`) after each string.
# 2. The `decode` method splits the encoded string by the special character to retrieve the original list of strings.
