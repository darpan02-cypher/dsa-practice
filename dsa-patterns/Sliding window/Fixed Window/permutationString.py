def permutationString(s: str, pattern: str) -> bool:
    window_start, matched = 0, 0
    char_frequency = {}

    for char in pattern:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True

        if window_end >= len(pattern) - 1:
            left_char = s[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return False

# Example usage
s = "oidbcaf"
pattern = "abc"
result = permutationString(s, pattern)
print(f"Does '{s}' contain a permutation of '{pattern}'? {result}")

#easy to remember approach: in short
#1. Create a frequency map of the characters in the pattern.
#2. Use a sliding window to traverse the string, adjusting the frequency map and matched count
#3. If the matched count equals the number of unique characters in the pattern, return True 