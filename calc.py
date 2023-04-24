from keybind import KeyBinder as bin
i = 1
while i >= 0:
    try:
        def dia():
            a = input("Number")
            print(eval(a))
        dia()

    except (NameError,SyntaxError,NameError):
        print("Error")
        dia()
bin.activate({
    'Esc':print("fsdfs")
}, run_thread=True)