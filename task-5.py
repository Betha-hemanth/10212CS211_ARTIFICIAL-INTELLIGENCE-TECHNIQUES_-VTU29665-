import random

# Travel duration between locations
distance = {
    "A": {"B": 10, "C": 15, "D": 20},
    "B": {"A": 10, "C": 35, "D": 25},
    "C": {"A": 15, "B": 35, "D": 30},
    "D": {"A": 20, "B": 25, "C": 30}
}

locations = list(distance.keys())

# ACO parameters
ants = 10
iterations = 50
evaporation = 0.5
alpha = 1
beta = 2
pheromone = 1.0

# Initialize pheromone
trail = {
    i: {j: pheromone for j in locations if j != i}
    for i in locations
}


def route_length(route):
    total = 0

    for i in range(len(route) - 1):
        total += distance[route[i]][route[i + 1]]

    # Return to starting location
    total += distance[route[-1]][route[0]]

    return total


def choose_next(current, unvisited):
    probabilities = []

    for city in unvisited:
        p = (trail[current][city] ** alpha) * \
            ((1 / distance[current][city]) ** beta)
        probabilities.append(p)

    return random.choices(unvisited, weights=probabilities)[0]


best_route = None
best_distance = float("inf")

# ACO iterations
for _ in range(iterations):

    all_routes = []

    for _ in range(ants):

        # Random starting location
        start = random.choice(locations)

        route = [start]
        unvisited = [x for x in locations if x != start]

        # Construct route
        while unvisited:
            next_city = choose_next(route[-1], unvisited)
            route.append(next_city)
            unvisited.remove(next_city)

        total = route_length(route)
        all_routes.append((route, total))

        # Update best route
        if total < best_distance:
            best_distance = total
            best_route = route

    # Pheromone evaporation
    for i in locations:
        for j in locations:
            if i != j:
                trail[i][j] *= (1 - evaporation)

    # Pheromone deposit
    for route, total in all_routes:
        deposit = 1 / total

        for i in range(len(route) - 1):
            a, b = route[i], route[i + 1]
            trail[a][b] += deposit
            trail[b][a] += deposit

        # Return edge
        a, b = route[-1], route[0]
        trail[a][b] += deposit
        trail[b][a] += deposit


# Display results
print("Best Route:", " -> ".join(best_route + [best_route[0]]))
print("Minimum Total Trip Duration:", best_distance)

print("\nFinal Pheromone Values:")
for i in locations:
    print(i, trail[i])
