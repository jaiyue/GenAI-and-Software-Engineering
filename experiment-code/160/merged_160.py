def do_algebra(operator, operand):
    expr = "".join(f"{operand[i]}{operator[i]}" for i in range(len(operator))) + str(operand[-1])
    return eval(expr)

