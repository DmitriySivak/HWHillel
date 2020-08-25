
if __name__ == '__main__':
    while True:
        operation = input("Enter arithmetic operation(+,-,*,/): ")
        if operation == 'exit':
            break
        if operation in ('+', '-', '*', '/'):
            var1 = float(input("First operand="))
            var2 = float(input("Second operand="))
            if operation == '+':
                print("%.2f" % (var1 + var2))
            elif operation == '-':
                print("%.2f" % (var1 - var2))
            elif operation == '*':
                print("%.2f" % (var1 * var2))
            elif operation == '/':
                if var2 != 0:
                    print("%.2f" % (var1 / var2))
        else:
                print("NOT arithmetic operation. Please, try again!")
