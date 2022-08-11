class Operator:
    def __init__(self, symbol, executor):
        self.symbol = symbol
        self.executor = executor
    
    def get_symbol(self): return self.symbol
    def get_executor(self): return self.executor

operator_array = [Operator("+", lambda a, b: a + b), Operator("-", lambda a, b: a - b)]
operator_dict = { i.get_symbol(): i for i in operator_array}

class Operation:
    def __init__(self, a, b, operator, width):
        self.a = a
        self.b = b
        self.operator = operator
        self.width = width

    def get_a(self): return self.a
    def get_b(self): return self.b
    def get_operator(self): return self.operator
    def get_width(self): return self.width

def contains_operator(function, operators):
    for operator in operators:
        ndx = function.find(operator)
        if ndx != -1:
            return operator, ndx
    return None

def arithmetic_arranger(functions, show_answer = False):
    functionArray = functions if functions is not None else []
    num_ops = len(functionArray)
    if num_ops > 5:
        return "Error: Too many problems."
    max_digits = 4
    op_separator_len = 4
    op_separator = " " * op_separator_len
    sum_index = 0
    subtract_index = 1
    operators = ["+", "-"]
    operations = []
    for current in functionArray:
        f = current.replace(" ", "")
        contains_operator_result = contains_operator(f, operators)
        if contains_operator_result == None:
            return "Error: Operator must be '+' or '-'."    
        operator = contains_operator_result[0]
        ndx = contains_operator_result[1]
        if (ndx > max_digits) or (len(f) - ndx - 1) > max_digits:
            return "Error: Numbers cannot be more than four digits."
        a = f[0:ndx]
        b = f[ndx + 1:]
        if not (a.isnumeric() and b.isnumeric()):
            return "Error: Numbers must only contain digits."
        width = max(ndx, len(f) - ndx - 1)
        operations.append(Operation(a = a, b = b, operator = operator, width = width))

    # return output lines
    resultStr = None
    if (num_ops > 0):
        first_line = ""
        second_line = ""
        third_line = ""
        fourth_line = "" if show_answer else None
        for i in range(0, len(operations)):
            curr_op = operations[i]
            first_line += "{addendum:>{width}}".format(addendum = curr_op.get_a(), width = curr_op.get_width() + 2)
            second_line += "{op} {addendum:>{width}}".format(op = curr_op.get_operator(), addendum = curr_op.get_b(), width = curr_op.get_width())
            third_line += "-" * (curr_op.get_width() + 2)
            if show_answer:
                result = operator_dict[curr_op.get_operator()].get_executor()(int(curr_op.get_a()), int(curr_op.get_b()))
                fourth_line += "{answ:>{width}}".format(answ = result, width = curr_op.get_width() + 2)
            if i < (len(operations) - 1):
                second_line += op_separator
                first_line += op_separator
                third_line += op_separator
                if show_answer:
                    fourth_line += op_separator
        resultStr = first_line + "\n" + second_line + "\n" + third_line
        if show_answer == True:
            resultStr += "\n" + fourth_line
    return resultStr
