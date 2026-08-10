graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)
        print(node, end=" ")
        for i in graph[node]:
            dfs(i)

print("DFS Traversal:")
dfs('A')
