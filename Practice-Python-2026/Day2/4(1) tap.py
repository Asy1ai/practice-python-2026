a = float(input("Бірінші сан: "))
b = float(input("Екінші сан: "))

operation = input("Операция (+, -, *, /): ")

if operation == "+":
    print(a+b)
elif operation == "-":
    print(a-b)
elif operation == "*":
    print(a*b)
elif operation == "/":
    print(a/b)

else:
    print("Қате операция")