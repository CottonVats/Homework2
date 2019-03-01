def polish(operation = str(input())):
    number1 = int(operation[1])
    number2 = int(operation[2])
    try:
        assert operation[0] in ("+", "-", "/", "*")
    except AssertionError:
        print("Эту операцию нельзя выполнить,извините")
    else:
        try:
            if operation[0] == "/":
                result = number1/number2
            elif operation[0] == "*":
                result = number1*number2
            elif operation[0] == "-":
                result = number1-number2
            elif operation[0] == "+":
                result = number1+number2
        except ZeroDivisionError:
            print("Вы делите на ноль")
        except TypeError:
            print("Вы делите строки или ввели не то количество аргументов")
        else:
            return result
print(polish())
