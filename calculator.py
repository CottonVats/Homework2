def polish(operation = str(input()), number1 = int(input()), number2 = int(input())):
    try:
        assert operation in ("+", "-", "/", "*")
    except AssertionError:
        print("Эту операцию нельзя выполнить,извините")
    else:
        try:
            if operation == "/":
                result = number1/number2
            elif operation == "*":
                result = number1*number2
            elif operation == "-":
                result = number1-number2
            elif operation == "+":
                result = number1+number2
        except ZeroDivisionError:
            print("Вы делите на ноль")
        except TypeError:
            print("Вы делите строки или ввели не то количество аргументов")
        else:
            return result
print(polish())
