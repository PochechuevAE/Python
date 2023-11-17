def hello(name):
    return "Hello " + name

def bye(name):
    return name + " bye"

def create_phrase(funcs):
    name = input("Введите свое имя: ")
    print("Это функция высшего порядка")
    res = ""
    for func in funcs:
        res += func(name) + "\n"
    return res

funcs = (hello, bye)
print(create_phrase(funcs))
