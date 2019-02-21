def polish(operation, number1, number2):
    try:
        assert operation == "+" or "-" or "/" or "*"
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
print(polish("/", 1, 5))
