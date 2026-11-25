
def alpha_beta(node, depth, alpha, beta, maximizing_player):

    if depth == 0 or isinstance(node, int):
        print("Leaf node:", node)
        return node

    if maximizing_player:
        best_value = float('-inf')
        print("\nMAX Player Turn")

        for child in node:
            value = alpha_beta(child, depth - 1, alpha, beta, False)

            best_value = max(best_value, value)
            alpha = max(alpha, best_value)

            print("Current Value:", value)
            print("Alpha:", alpha)
            print("Beta:", beta)

            if alpha >= beta:
                print("Pruning occurs!")
                break

        print("MAX returns:", best_value)
        return best_value

    else:
        best_value = float('inf')
        print("\nMIN Player Turn")

        for child in node:
            value = alpha_beta(child, depth - 1, alpha, beta, True)

            best_value = min(best_value, value)
            beta = min(beta, best_value)

            print("Current Value:", value)
            print("Alpha:", alpha)
            print("Beta:", beta)

            if alpha >= beta:
                print("Pruning occurs!")
                break

        print("MIN returns:", best_value)
        return best_value


tree = [
    [3, 5, 6],
    [9, 1, 2],
    [0, -1, 4]
]

print("Starting Alpha-Beta Pruning")

result = alpha_beta(
    tree, 2,
    float('-inf'),
    float('inf'),
    True
)

print("\n----------------------")
print("Final Optimal Value:", result)
print("Alpha-Beta Pruning Completed")
