result = None
operand = None
operator = None
wait_for_number = True
while True:
    user_input = input(">>> ")
    if wait_for_number:
        try:
            operand = float(user_input)
        except ValueError:
            print("Not a Number")
            continue
        wait_for_number = False
        if not result:
            result = operand
        elif operator == "=":
            print(result)
            break
        else:
            if operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
            elif operator == "*":
                result = result * operand
            elif operator == "/":
                try:
                    result = result / operand
                except ZeroDivisionError:
                    print("Ділення на 0")
                    continue
    else:
        if user_input in ('+', '-', '*', '/'):
            operator = user_input
        else:
            operator = None
        if not operator:
            print("Not operator")
        else:
            wait_for_number = True
