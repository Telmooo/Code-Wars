import operator

def basic_op(ops, value1, value2):
    operators = {"+": operator.add, "-": operator.sub,
                "*": operator.mul, "/": operator.truediv,
                "**": operator.pow, "//": operator.floordiv,
                "%": operator.mod}
    return operators[ops](value1, value2)
