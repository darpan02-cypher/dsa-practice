def bfs(graph, start_node):
    visited = set()
    queue = [start_node]
    visited.add(start_node)

    while queue:
        current_node = queue.pop(0)
        print(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

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