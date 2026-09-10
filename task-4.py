# Mini-Max Algorithm with Alpha-Beta Pruning
# Treasure Hunt Game

tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [3, 5],
    "E": [6, 9],
    "F": [1, 2],
    "G": [0, 1]
}

pruned = []


def minimax(node, maximizing, alpha, beta):
    # Leaf node
    if isinstance(node, int):
        return node

    if maximizing:
        best = float("-inf")

        for child in tree[node]:
            value = minimax(child, False, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                # Remaining children are pruned
                remaining = tree[node][tree[node].index(child) + 1:]
                pruned.extend(remaining)
                break

        return best

    else:
        best = float("inf")

        for child in tree[node]:
            value = minimax(child, True, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                remaining = tree[node][tree[node].index(child) + 1:]
                pruned.extend(remaining)
                break

        return best


# Initial values
alpha = float("-inf")
beta = float("inf")

# Calculate Mini-Max value
value = minimax("A", True, alpha, beta)

# Find best move
best_move = max(
    tree["A"],
    key=lambda child: minimax(child, False, float("-inf"), float("inf"))
)

print("Mini-Max Value:", value)
print("Best Move:", best_move)
print("Pruned Branches:", pruned)
