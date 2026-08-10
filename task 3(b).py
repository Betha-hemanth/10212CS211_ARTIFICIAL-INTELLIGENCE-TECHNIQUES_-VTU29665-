from queue import PriorityQueue

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

h = {'A':7, 'B':6, 'C':4, 'D':4, 'E':2, 'F':1, 'G':0}

def astar(start, goal):
    q = PriorityQueue()
    q.put((h[start], 0, start, [start]))
    visited = []

    while not q.empty():
        f, g, node, path = q.get()

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Cost:", g)
            return

        if node in visited:
            continue
        visited.append(node)

        for nxt, cost in graph[node]:
            if nxt not in visited:
                ng = g + cost
                q.put((ng + h[nxt], ng, nxt, path + [nxt]))

astar('A', 'G')
