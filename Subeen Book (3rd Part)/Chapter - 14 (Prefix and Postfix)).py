# গাণিতিক রাশির মান.
# Accept the mathematical sum.

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


