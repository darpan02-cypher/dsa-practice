from ast import List
from collections import Counter


def findAllAnagrams(s: str, p: str) :

    #edge case 
    if len(p) > len(s):
        return []

    # Initialize the frequency map for the pattern string
    p_count = Counter(p)
    window= Counter(s[:len(p)])

    answer = []
    if window == p_count:
        answer.append(0)
    for i in range(len(p), len(s)):
        # Add the new character to the window
        window[s[i]] += 1
        # Remove the character that is no longer in the window
        window[s[i - len(p)]] -= 1

        # If the count of the character becomes zero, remove it from the window
        if window[s[i - len(p)]] == 0:
            del window[s[i - len(p)]]

        # Compare the current window with the pattern's frequency map
        if window == p_count:
            answer.append(i - len(p) + 1)

    return answer       
## Example usage
s = "cbaebabacd"
p = "abc"
result = findAllAnagrams(s, p)
print(f"All starting indices of anagrams of '{p}' in '{s}' are: {result}")  # Output: All starting indices of anagrams of 'abc' in 'c
    