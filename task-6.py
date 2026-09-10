colors = ["Red", "Green", "Blue", "Yellow"]

neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E"],
    "E": ["C", "D"]
}

assignment = {}

def valid(zone, color):
    return all(assignment.get(n) != color for n in neighbors[zone])

def solve():
    if len(assignment) == 5:
        return True

    for zone in neighbors:
        if zone not in assignment:
            for color in colors:
                if valid(zone, color):
                    assignment[zone] = color

                    if solve():
                        return True

                    del assignment[zone]
            return False

solve()

print("Valid Color Assignment:")
for zone, color in assignment.items():
    print(zone, "->", color)
