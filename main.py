try:
    a = float(input("number:"))
    b = str(input("dia:"))
    c = float(input("number:"))
except ValueError:
    a = float(input("number:"))
    b = str(input("dia:"))
    c = float(input("number:"))
    print("У вас ошибка в воде попробуйте заного")

def dia():
    a = float(input("number:"))
    b = str(input("dia:"))
    c = float(input("number:"))


if (b == "*"):
    print(a*c)
elif (b == "/"):
    print(a/c)
elif (b == "-"):
    print(a-c)
elif(b == "+"):
    print(a+c)
else:
    dia()

