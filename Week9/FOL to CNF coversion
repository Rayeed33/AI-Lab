
def eliminate_implication(expr):
    if isinstance(expr, str):
        return expr

    op = expr[0]

    if op == "->":
        p = eliminate_implication(expr[1])
        q = eliminate_implication(expr[2])
        return ("OR", ("NOT", p), q)

    if op == "NOT":
        return ("NOT", eliminate_implication(expr[1]))

    return (op,) + tuple(
        eliminate_implication(x) for x in expr[1:]
    )


def move_negation(expr):
    if isinstance(expr, str):
        return expr

    op = expr[0]

    if op == "NOT":
        child = expr[1]

        if isinstance(child, str):
            return expr

        if child[0] == "NOT":
            return move_negation(child[1])

        if child[0] == "AND":
            return (
                "OR",
                move_negation(("NOT", child[1])),
                move_negation(("NOT", child[2]))
            )

        if child[0] == "OR":
            return (
                "AND",
                move_negation(("NOT", child[1])),
                move_negation(("NOT", child[2]))
            )

    return (op,) + tuple(move_negation(x) for x in expr[1:])


def distribute_or(expr):
    if isinstance(expr, str):
        return expr

    op = expr[0]

    if op == "OR":
        a = distribute_or(expr[1])
        b = distribute_or(expr[2])

        if isinstance(a, tuple) and a[0] == "AND":
            return (
                "AND",
                distribute_or(("OR", a[1], b)),
                distribute_or(("OR", a[2], b))
            )

        if isinstance(b, tuple) and b[0] == "AND":
            return (
                "AND",
                distribute_or(("OR", a, b[1])),
                distribute_or(("OR", a, b[2]))
            )

        return ("OR", a, b)

    return (op,) + tuple(distribute_or(x) for x in expr[1:])


def display(expr):
    if isinstance(expr, str):
        return expr

    op = expr[0]

    if op == "NOT":
        return "~" + display(expr[1])

    if op in ("AND", "OR"):
        symbol = " AND " if op == "AND" else " OR "
        return "(" + display(expr[1]) + symbol + display(expr[2]) + ")"

    return str(expr)


# Input: P -> (Q AND R)
expression = (
    "->",
    "P",
    ("AND", "Q", "R")
)

print("Original Expression:")
print(display(expression))

step1 = eliminate_implication(expression)
print("\nAfter Eliminating Implication:")
print(display(step1))

step2 = move_negation(step1)
print("\nAfter Moving Negation Inward:")
print(display(step2))

step3 = distribute_or(step2)
print("\nAfter Distributing OR over AND:")
print(display(step3))

print("\nFinal CNF Expression:")
print(display(step3))
