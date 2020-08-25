from calculator import add, divide, multiply, substraction

if __name__ == '__main__':
    var1 = 0
    var2 = 0
    oper = ' '

    print("Enter first operand:")
    while 1:
        var1 = input()
        if var1.isdigit():
            var1 = int(var1)
            break
        else:
            print("NOT numerical expression.Please, try again")
            continue

    print("Enter arithmetic operation:")
    while 1:
        oper = input()
        if oper == '+' or oper == '-' or oper == '*' or oper == '/' or oper == 'exit':
            break
        else:
            print("NOT arithmetic operation. Please, try again")

    print("Enter second operand:")
    while 1:
        var2 = input()
        if var2.isdigit():
            var2 = int(var2)
            break
        else:
            print("NOT numerical expression.Please, try again")
            continue

if oper == '+':
    print(add.add(var1, var2))
if oper == '-':
    print(substraction.sub(var1, var2))
if oper == '*':
    print(multiply.mul(var1, var2))
if oper == '/':
    print(divide.div(var1, var2))
if oper == "exit":
    exit()
