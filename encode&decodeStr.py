from typing import List
#Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

class Solution:     #this solution was not accepted , but below then this code is accepted solution because it is safe and does not use any special character to join the strings

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
#Bonus safe version -- accepted solution
###########################
'''class Solution:

    def encode(self, strs: List[str]) -> str:
        # Store each string as: length_of_string + '#' + string
        # Step 1: For each string, get its length and concatenate with '#' and the string itself
        encoded_pieces = []  # List to hold encoded pieces
        for s in strs:
            length = len(s)
            encoded_piece = f"{length}#{s}"
            encoded_pieces.append(encoded_piece)
        # Step 2: Join all encoded pieces into a single string
        return ''.join(encoded_pieces)
        #return ''.join(f"{len(s)}#{s}" for s in strs)


    def decode(self, s: str) -> List[str]:
        res = []  # List to hold decoded strings
        i = 0
        # Step 3: Iterate through the encoded string to extract each piece
        # Step 4: Use a while loop to find each encoded piece
        # Step 5: Extract the length and the string based on the separator '#'
        # Step 6: Append the extracted string to the result list
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