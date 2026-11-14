# Simple singly linked list

class Node:
    def __init__(self, val): # constructor to initialize the node with a pointer to the next node
        self.val = val   # self is used to refer to the current instance of the class
        self.next = None # initialize the next pointer to None



# create new nodes manually
node1 = Node(1) #Step 1: Create a node with value 1
node2 = Node(2)
node3 = Node(3) 

# link the nodes together
node1.next = node2 #Step 2: Link node1 to node2
node2.next = node3# Step 3: Link node2 to node3

current = node1 # start from the head of the linked list
while current is not None: # Step 4: Traverse the linked list until the end
    print(current.val) # print the value of the current node
    current = current.next # move to the next node

# Easy to remeber Pseodo code for linked list implementation:
# 1. Create a node (example syntax - node = Node(value))
# 2. Initialize the node with a value and a pointer to the next node
# 3. Link the nodes together
# 4. Traverse the linked list

