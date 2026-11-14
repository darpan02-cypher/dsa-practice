class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# Outside the classes, properly unindented:
values = [1, 2, 3, 4, 5]
ll = LinkedList()
for val in values:
    ll.append(val)

middle = ll.find_middle()
print(middle.val if middle else None)

# Traverse from the middle node to the end
res = []
curr = middle
while curr:
    res.append(curr.val)
    curr = curr.next

print(res)  # Output: [3, 4, 5]