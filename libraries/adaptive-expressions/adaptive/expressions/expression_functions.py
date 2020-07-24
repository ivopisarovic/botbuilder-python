from .expression_type import ADD, SUBTRACT, MULTIPLY, DIVIDE, EQUAL, LESSTHEN
from .builtin_functions.add import Add
from .builtin_functions.subtract import Subtract
from .builtin_functions.multiply import Multiply
from .builtin_functions.divide import Divide
from .builtin_functions.equal import Equal
from .builtin_functions.less_then import LessThen
from .builtin_functions.min import Min
from .builtin_functions.max import Max
from .builtin_functions.power import Power


def get_standard_functions() -> dict:
    functions = []
    functions.append(Add())
    functions.append(Subtract())
    functions.append(Multiply())
    functions.append(Divide())
    functions.append(Equal())
    functions.append(LessThen())
    functions.append(Min())
    functions.append(Max())
    functions.append(Power())

    lookup = dict()
    for function in functions:
        lookup[function.expr_type] = function

    lookup["add"] = lookup[ADD]
    lookup["equal"] = lookup[EQUAL]
    lookup["lessthen"] = lookup[LESSTHEN]
    lookup["sub"] = lookup[SUBTRACT]
    lookup["mul"] = lookup[MULTIPLY]
    lookup["div"] = lookup[DIVIDE]

    return lookup


class ExpressionFunctions:
    standard_functions = staticmethod(get_standard_functions())
