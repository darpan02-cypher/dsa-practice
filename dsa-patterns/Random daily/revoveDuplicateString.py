def removeDuplicateString(s):
    # Create a set to store unique characters
    unique_chars = set()
    
    # Iterate through the string and add characters to the set
    for char in s:
        unique_chars.add(char)
    
    # Convert the set back to a string and return it
    return ''.join(unique_chars)

#time complexity is O(n) where n is the length of the string
#example usage
input_string = "hello world"
result = removeDuplicateString(input_string)
print(f"The string after removing duplicates is: {result}")