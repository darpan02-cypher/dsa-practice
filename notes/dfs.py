def dfs(graph, start_node):
    visited = set()  # why set - it does not count duplicates then? - Because a set automatically handles uniqueness, ensuring each node is visited only once.
    stack = [start_node]  # stack - as a list to store nodes to be visited, (In python we use a list as a stack, unless we use collections.deque)
    visited.add(start_node)

    while stack:
        current_node = stack.pop()  # Pop a node from the top of the stack - this will process nodes in a depth-first manner (LIFO)
        print(current_node)

        # Check all unvisited neighbors
        for neighbor in graph[current_node]:  # Iterate through each neighbor of the current node
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)  # Add to top

# Example usage:
if __name__ == "__main__":  
    # Example usage (graph as dict):
    # graph = {
    #     'A': ['B', 'C'],
    #     'B': ['A', 'D', 'E'],
    #     'C': ['A', 'F'],
    #     'D': ['B'],
    #     'E': ['B', 'F'],
    #     'F': ['C', 'E']
    # }
    # dfs(graph, 'A')

    # If we have a list of edges, convert it into an adjacency list:
    graph = {}
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F')]
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    dfs(graph, 'A')


    #difference between dfs and bfs - i dont see any difference when i look at the code - the difference is in the data structure used to store nodes to be visited. In BFS, we use a queue (FIFO) to explore nodes level by level, while in DFS, we use a stack (LIFO) to explore as deep as possible along each branch before backtracking. This leads to different traversal orders and can affect the pathfinding and search results in various applications.
    # but in python we are using list only in both cases - yes, but the way we use the list is different. In BFS, we pop from the front (index 0) to simulate a queue, while in DFS, we pop from the end (last index) to simulate a stack. This difference in popping behavior leads to the distinct traversal patterns of BFS and DFS.
    #how ...code for pop is different in both cases - In BFS, we use `queue.pop(0)` to remove the first element from the list, simulating a queue (FIFO). In DFS, we use `stack.pop()` to remove the last element from the list, simulating a stack (LIFO). This difference in how we remove elements from the list is what creates the distinct traversal patterns of BFS and DFS.