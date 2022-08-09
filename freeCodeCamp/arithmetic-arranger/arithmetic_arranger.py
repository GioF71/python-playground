class OpDef:
    def __init__(self, a, b, op):
        self.a = a
        self.b = b
        self.op = op

    def get_a(self): return self.a
    def get_b(self): return self.b
    def get_op(self): return self.op

def arithmetic_arranger(functions, show_answer = False):
    num_ops = len(functions) if functions is not None else 0
    if num_ops > 5:
        return "Error: Too many problems."
    max_digits = 4
    op_separator_len = 4
    op_separator = " " * op_separator_len
    sum_index = 0
    subtract_index = 1
    operators = ["+", "-"]
    op_data = []
    bList = []
    opList = []
    wList = []
    resultList = []
    for current in functions if functions is not None else []:
        f = current.replace(" ", "")
        op = None
        ndx = f.find("+")
        if ndx != -1:
            op = sum_index
        else:
            ndx = f.find("-")
            if (ndx != -1):
                op = subtract_index
            else:
                return "Error: Operator must be '+' or '-'."
        if (ndx) > max_digits or (len(f) - ndx - 1) > max_digits:
            return "Error: Numbers cannot be more than four digits."
        a = f[0:ndx]
        b = f[ndx + 1:]
        if not (a.isnumeric() and b.isnumeric()):
            return "Error: Numbers must only contain digits."
        result = (int(a) + int(b)) if op == 0 else int(a) - int(b)
        resultList.append(result)
        w = max(ndx, len(f) - ndx - 1)
        bList.append(b)
        opList.append(op)
        wList.append(w)
        op_data.append(OpDef(a, b, op))

    # print lines
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    for i in range(0, len(op_data)):
        first_line += "{addendum:>{width}}".format(addendum = op_data[i].get_a(), width = wList[i] + 2)
        second_line += "{op} {addendum:>{width}}".format(op = operators[op_data[i].get_op()], addendum = op_data[i].get_b(), width = wList[i])
        third_line += "-" * (wList[i] + 2)
        if show_answer:
            fourth_line += "{answ:>{width}}".format(answ = resultList[i], width = wList[i] + 2)
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
