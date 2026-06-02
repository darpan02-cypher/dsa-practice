arr = [] # Empty array initialization

freq = {} # Empty dictionary initialization

seen = set() 

stack = [] #

from collections import deque
queue = deque() 

from collections import defaultdict
graph = defaultdict(list)

freq = defaultdict(int)

from collections import Counter
count = Counter(nums)

import heapq
heap = []

grid = [[0] * cols for _ in range(rows)]



#++++++++++++++++++++++In details about initialization for different data structures++++++++++++++++++++++#

# =====================================================
# 1. ARRAY / LIST
# =====================================================

arr = []                    # Empty array
arr = [1, 2, 3]             # Initialize with values
arr = [0] * 5               # [0,0,0,0,0]

# 2D Array (IMPORTANT)
grid = [[0] * 3 for _ in range(4)]

# DON'T DO THIS
# grid = [[0] * 3] * 4
# All rows point to same memory


#Use Aray when - 
# You need O(1) access by index
# You need to store homogeneous data types - same type
# Use List when -
# You need dynamic resizing
# You need to store heterogeneous data types - different types

#very imp to note in python 
'''In Python, standard syntax like arr = [1, 2, 3] always creates a List, which gives you both $O(1)$ indexing and dynamic resizing automatically.You only need to change your declaration syntax if you explicitly import specialized modules like array or numpy to enforce strict type homogeneity for memory optimization.
Otherwise its just creating list by default which is dynamic array in python.'''
# =====================================================
# 2. STRING
# =====================================================

s = "hello"

# Strings are IMMUTABLE
# s[0] = 'H' ❌

# Build strings efficiently
chars = []
chars.append("a")
chars.append("b")

result = "".join(chars)


# =====================================================
# 3. HASHMAP / DICTIONARY
# =====================================================

freq = {}

# Insert / Update
freq["apple"] = 1

# Safe access
count = freq.get("apple", 0)

# Frequency counting pattern
for num in nums:
    freq[num] = freq.get(num, 0) + 1

# Use hashmap/dictionary when:
# You need O(1) average case access by key
# You need to store key-value pairs


# =====================================================
# 4. DEFAULTDICT
# =====================================================

from collections import defaultdict

# Auto initialize integer values to 0
freq = defaultdict(int)

freq[5] += 1

# Auto initialize lists
graph = defaultdict(list)

graph[1].append(2)


# =====================================================
# 5. SET
# =====================================================

seen = set()

seen.add(5)

if 5 in seen:
    pass

seen.remove(5)

# Used for:
# Duplicate detection
# Visited nodes in graph/tree

# Use set when:
# You need O(1) average case membership testing - "x in seen"
# You need to store unique elements



# =====================================================
# 6. STACK (LIFO)
# =====================================================

stack = []

# Push
stack.append(10)

# Pop
stack.pop()

# Peek. --> Look at the top element without removing it
top = stack[-1]

# Used in:
# DFS
# Monotonic Stack
# Parentheses problems


# =====================================================
# 7. QUEUE (FIFO)
# =====================================================

from collections import deque

queue = deque()

# Enqueue
queue.append(10)

# Dequeue
queue.popleft()

# Used in:
# BFS
# Level Order Traversal


# =====================================================
# 8. DEQUE
# =====================================================

from collections import deque

dq = deque()

dq.append(1)
dq.appendleft(0)

dq.pop()
dq.popleft()

# Used in:
# Sliding Window Maximum
# BFS


# =====================================================
# 9. HEAP / PRIORITY QUEUE
# =====================================================

import heapq

heap = []

# Push
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)

# Pop smallest
smallest = heapq.heappop(heap)

# Max Heap Trick
heapq.heappush(heap, -10)

largest = -heapq.heappop(heap)

# Used in:
# Top K Elements
# Dijkstra
# Scheduling


# =====================================================
# 10. COUNTER
# =====================================================

from collections import Counter

count = Counter(nums)

# Frequency of element
count[5]

# Top K frequent
count.most_common(3)

# Used in:
# Frequency problems
# Anagrams

#Use counter when:
# You need to count frequencies of elements in an iterable- 



# =====================================================
# 11. LINKED LIST NODE
# =====================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Dummy Node Pattern
dummy = ListNode(0)
curr = dummy

# Build list
curr.next = ListNode(1)
curr = curr.next

# Return answer
head = dummy.next

# Used in:
# Merge Lists
# Remove Nodes
# Reverse List


# =====================================================
# 12. BINARY TREE NODE
# =====================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Used in:
# DFS
# BFS
# Tree Recursion


# =====================================================
# 13. GRAPH (Adjacency List)
# =====================================================

from collections import defaultdict

graph = defaultdict(list)

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)   # Remove if directed graph

# Used in:
# DFS
# BFS
# Dijkstra
# Topological Sort


# =====================================================
# 14. VISITED SET
# =====================================================

visited = set()

visited.add(node)

if node in visited:
    return

# Used in:
# Graph Traversal
# Cycle Detection


# =====================================================
# 15. MATRIX / GRID
# =====================================================

rows = len(grid)
cols = len(grid[0])

# 4-direction movement
directions = [
    (1, 0),   # Down
    (-1, 0),  # Up
    (0, 1),   # Right
    (0, -1)   # Left
]

for dr, dc in directions:
    nr = r + dr
    nc = c + dc

# Used in:
# Number of Islands
# Flood Fill
# Shortest Path in Grid