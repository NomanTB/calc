i = 1
while i >= 0:
    try:
        def dia():
            a = input("Number")
            print(eval(a))
        dia()

    except NameError:
        print("Было введено текст а не числа")
        dia()
