def do_algebra(operator, operand):
    expr = "".join(f"{operand[i]}{operator[i]}" for i in range(len(operator))) + str(operand[-1])
    return eval(expr)

# Builds the expression from the lists and uses Python's evaluator (honors **, //, *, +, - precedence).

