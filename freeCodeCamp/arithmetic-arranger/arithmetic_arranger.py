class Operator:
    def __init__(self, symbol, executor):
        self.symbol = symbol
        self.executor = executor
    
    def get_symbol(self): return self.symbol
    def get_executor(self): return self.executor

operator_array = [Operator("+", lambda a, b: a + b), Operator("-", lambda a, b: a - b)]
operator_dict = { i.get_symbol(): i for i in operator_array}

class OpDef:
    def __init__(self, a, b, operator, width, result):
        self.a = a
        self.b = b
        self.operator = operator
        self.width = width
        self.result = result

    def get_a(self): return self.a
    def get_b(self): return self.b
    def get_operator(self): return self.operator
    def get_width(self): return self.width
    def get_result(self): return self.result

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
    op_data = []
    op_operator = None
    for current in functionArray:
        f = current.replace(" ", "")
        contains_operator_result = contains_operator(f, operators)
        if contains_operator_result == None:
            return "Error: Operator must be '+' or '-'."    
        op_operator = contains_operator_result[0]
        ndx = contains_operator_result[1]
        if (ndx > max_digits) or (len(f) - ndx - 1) > max_digits:
            return "Error: Numbers cannot be more than four digits."
        a = f[0:ndx]
        b = f[ndx + 1:]
        if not (a.isnumeric() and b.isnumeric()):
            return "Error: Numbers must only contain digits."
        result = operator_dict[op_operator].get_executor()(int(a), int(b))
        width = max(ndx, len(f) - ndx - 1)
        op_data.append(OpDef(a = a, b = b, operator = op_operator, width = width, result = result))

    # return output lines
    resultStr = None
    if (num_ops > 0):
        first_line = ""
        second_line = ""
        third_line = ""
        fourth_line = "" if show_answer else None
        for i in range(0, len(op_data)):
            first_line += "{addendum:>{width}}".format(addendum = op_data[i].get_a(), width = op_data[i].get_width() + 2)
            second_line += "{op} {addendum:>{width}}".format(op = op_data[i].get_operator(), addendum = op_data[i].get_b(), width = op_data[i].get_width())
            third_line += "-" * (op_data[i].get_width() + 2)
            if show_answer:
                fourth_line += "{answ:>{width}}".format(answ = op_data[i].get_result(), width = op_data[i].get_width() + 2)
            if i < (len(op_data) - 1):
                second_line += op_separator
                first_line += op_separator
                third_line += op_separator
                if show_answer:
                    fourth_line += op_separator
        resultStr = first_line + "\n" + second_line + "\n" + third_line
        if show_answer == True:
            resultStr += "\n" + fourth_line
    return resultStr
