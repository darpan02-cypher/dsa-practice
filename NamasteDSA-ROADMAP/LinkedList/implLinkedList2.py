class Node:                             # Blueprint for an individual node: [ val | next ]
    def __init__(self, val):            # Constructor triggered when Node(val) is called
        self.val = val                  # Stores the data inside the node:  [ 1 | ... ]
        self.next = None                # Pointer to the next node:       [ 1 | None ]

class LinkedList:                       # User-defined wrapper class to manage the chain of nodes
    def __init__(self):                 # Constructor triggered when LinkedList() is called
        self.head = None                # Tracks the start of the list:   head -> None (empty list)
    def append(self, val):
        new_node = Node(val)  # Create a new node with the given value
        if self.head is None:  # If the linked list is empty
            self.head = new_node  # Set the new node as the head of the list
        else:
            current = self.head  # Start from the head of the list
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Link the last node to the new node

    def display(self):
        current = self.head  # Start from the head of the list
        while current:  # Traverse the list until the end
            print(current.val, end=" -> ")  # Print the value of the current node
            current = current.next
        print("None")  # Indicate the end of the list

# Example usage:
ll = LinkedList()  # Create a new linked list
ll.append(1)  # Append values to the linked list
ll.append(2)
ll.append(3)    
ll.display()  # Display the linked list