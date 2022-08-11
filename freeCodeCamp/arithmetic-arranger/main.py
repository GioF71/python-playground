# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger
from arithmetic_arranger import Operator
from arithmetic_arranger import contains_operator

print(contains_operator("32+698", ["+", "-"]))
print(contains_operator("3230-698", ["+", "-"]))
print(contains_operator("3230*698", ["+", "-"]))


operator_array = [Operator("+", lambda a, b: a + b), Operator("-", lambda a, b: a - b)]
operator_dict = { i.get_symbol(): i for i in operator_array}

#print(operator_array[0].get_executor()(3, 5))
print(operator_dict["+"].get_executor()(3, 5))

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))

print(arithmetic_arranger(['3801 - 2', '123 + 49'], False))

print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))

print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
# Run unit tests automatically
main(['-vv'])
