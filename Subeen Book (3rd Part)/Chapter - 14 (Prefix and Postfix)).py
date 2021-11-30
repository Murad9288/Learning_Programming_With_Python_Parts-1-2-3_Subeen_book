# গাণিতিক রাশির মান.
# পরিশিষ্ট
# Accept the mathematical sum.

# Books code:
# Prefix expression.

def operation_(operand_1,operand_2,operator):
    if operator == "+":
        return int(operand_1) + int(operand_2)
    elif operator == "-":
        return int(operand_1) - int(operand_2)
    elif operator == "*":
        return  int(operand_1) * int(operand_2)
    else:
        return int(operand_1) / int(operand_2)

def prefix(operation):
    operand = []
    operator = "+-*/"
    for char in operation:

        if char in operator:
            operand_2 = operand.pop()
            operand_1 = operand.pop()
            result = operation_(operand_1,operand_2,char)
            operand.append(str(result()))
        elif char.isdigit():
            operand.append(char)

    result = operand.pop()
    return result
operation = "3","2","-"
print(prefix(operation))


# Prefix expression:
# My code:
'''
s = input()
special_char = "+-*/"
prefix = ""
for i in s:
    if i.isdigit():
        prefix += i
for j in s:
    if j in special_char:
        prefix += j
print("Prefix Expression: %s"%prefix)

'''

# Books code:
# Postfix expression.
'''
def operation(op_1,op_2,op_3):
    return eval(op_1+op_2+op_3)

def postfix(op):
    operand = []
    operator = ["+","/","-","*"]
    op_list = op.split(",")
    for item in op_list:
        if item in operator:
            op_2 = operand.pop()
            op_1 = operand.pop()
            result = operation(op_1,op_2,item)
            operand.append(str(result))
        else:
            operand.append(item)
    result = operand.pop()
    return result

op = "20,30,+,2,*,10,*,4,/"
result = postfix(op)
print(result)
'''

# Postfix expression:
# My code:
'''
s = input()
special_char = "+-*/"
postfix = ""
for i in s:
    if i in special_char:
        postfix += i
for j in s:
    if j.isdigit():
        postfix += j
print("Postfix Expression: %s"%postfix)
'''
# My name is Murad.
# Email = muradhossainm01@gmail.com
# Thank you. All the best. and best of luck everytime...
