def removeDuplicates(arr):
    # Create a set to store unique elements
    unique_elements = set()
    
    # Iterate through the array and add elements to the set
    for element in arr:
        unique_elements.add(element)
    
    # Convert the set back to a list and return it
    return list(unique_elements)