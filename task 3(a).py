from queue import PriorityQueue

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

h = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}

def astar(start, goal):
    pq = PriorityQueue()
    pq.put((h[start], 0, start, [start]))
    visited = set()

    while not pq.empty():
        f, g, node, path = pq.get()

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Cost:", g)
            return

        if node in visited:
            continue
        visited.add(node)

        for nxt, cost in graph[node]:
            if nxt not in visited:
                ng = g + cost
                nf = ng + h[nxt]
                pq.put((nf, ng, nxt, path + [nxt]))

astar('A', 'G')
