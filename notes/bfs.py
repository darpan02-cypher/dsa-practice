def bfs(graph, start_node):
    visited = set()  # why set - it does not cunt duplicates then? - Because a set automatically handles uniqueness, ensuring each node is visited only once.
    queue = [start_node]  # queue - as a list to store nodes to be visited, (In python we use a list as a queue, unless we use collections.deque)
    visited.add(start_node)

    while queue:
        current_node = queue.pop(0) # Dequeue a node from the front of the queue - this will process nodes in a breadth-first manner (FIFO)
        print(current_node)

        # Check all unvisited neighbors
        for neighbor in graph[current_node]: # Iterate through each neighbor of the current node
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor) #  Add to back

   

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
    # bfs(graph, 'A')

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

    bfs(graph, 'A')


#in simple bfs template to remember lifelong -
# 1. Initialize visited set and queue - (You need to keep track of visited nodes to avoid cycles and a queue to explore nodes level by level. )
# 2. Start with the initial node - Add the starting node to the queue and mark it as visited.
# 3. While the queue is not empty - Continue exploring until there are no more nodes to visit.
# 4. Dequeue a node - Remove the front node from the queue and process it (e.g., print it).
# 5. Explore neighbors - For each neighbor of the current node, if it hasn't been visited, mark it as visited and add it to the queue for future exploration.
# 6. Repeat - Go back to step 3 until all reachable nodes have been visited.

# Link video - https://www.youtube.com/watch?v=pcKY4hjDrxk&t=246s 