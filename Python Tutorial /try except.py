try:
    value = 10/0
    number = float(input("enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by Zero")
except ValueError:
    print("invalid input")