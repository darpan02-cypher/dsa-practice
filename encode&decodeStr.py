from typing import List
#Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Join the strings with a special character that won't appear in the strings
        # Step 1: Initialize an empty string to store the result
        result = ''
        # Step 2: Loop through each string in the list
        for s in strs:
            # Step 3: Add the string and a '#' separator to the result for identification later
            result += s + '#'   #or result= result + s + #
        # Step 4: Return the final encoded string
        return result

    def decode(self, decode_str: str) -> List[str]:
        # Split the string by the special character to get the original strings
        return decode_str.split('#')[:-1]  #spliting by '#' and removing the last empty string as it will be added after the last string


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


###########################
#Bonus safe version
###########################
'''class Solution:

    def encode(self, strs: List[str]) -> str:
        # Store each string as: length_of_string + '#' + string
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # Move j to find the separator #
            while s[j] != '#':
                j += 1
            length = int(s[i:j])          # Get the length
            res.append(s[j+1:j+1+length]) # Extract the string
            i = j + 1 + length            # Move to next block
        return res
'''