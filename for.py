n = int(input("Enter: "))
operator = str(input("Choose operator: "))

if operator == "*" or operator == "/":
    result = 1
elif operator == "+" or operator == "-":
    result = 0
else:
    print("Probably, you entered wrong operator.")
    result = 0
try:
    for i in range(n):
        num = int(input("Enter: "))
        if operator == "+":
            result += num
        elif operator == "-":
            result -= num
        elif operator == "*":
            result *= num
        elif operator == "/":
            result /= num

    print("Result =", result)
    print("Continue? (y/n)")

    user_answer = str(input())

    while user_answer == "y":
        n = int(input("Enter: "))
        operator = str(input("Choose operator: "))

        if operator == "*" or operator == "/":
            result = 1
        elif operator == "+" or operator == "-":
            result = 0
        else:
            print("Probably, you entered wrong operator.")
            result = 0

        for i in range(n):
            num = int(input("Enter: "))
            if operator == "+":
                result += num
            elif operator == "-":
                result -= num
            elif operator == "*":
                result *= num
            elif operator == "/":
                result /= num

        print("Result =", result)
        print("Continue? (y/n)")

        user_answer = str(input())
    else:
        print("Bye!")
except ZeroDivisionError:
    print("You can't devide by zero!")

