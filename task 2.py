import random

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def cost(path):
    c = 0
    for i in range(len(path) - 1):
        c += graph[path[i]][path[i + 1]]
    c += graph[path[-1]][path[0]]
    return c

def hill_climb():
    path = [0, 1, 2, 3]
    best = cost(path)

    while True:
        improved = False
        for i in range(1, len(path)):
            for j in range(i + 1, len(path)):
                new = path[:]
                new[i], new[j] = new[j], new[i]
                new_cost = cost(new)

                if new_cost < best:
                    path = new
                    best = new_cost
                    improved = True

        if not improved:
            break

    print("Best Path:", path + [path[0]])
    print("Minimum Cost:", best)

hill_climb()
