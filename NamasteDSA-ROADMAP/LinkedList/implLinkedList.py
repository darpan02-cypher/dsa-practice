# Simple singly linked list

class Node:
    def __init__(self, val):
        self.val = val   # self is used to refer to the current instance of the class
        self.next = None # initialize the next pointer to None

class LinkedList:
    pass

# create new nodes manually
node1 = Node(1)
node2 = Node(2)
node3 = Node(3) 

# link the nodes together
node1.next = node2
node2.next = node3

current = node1 # start from the head of the linked list
while current is not None:
    print(current.val) # print the value of the current node
    current = current.next # move to the next node