# def f(x):
#     return x*x
# a = f
# print(type(f))
# print(type(a))
# print(a(5))
# print(f(5))

# def calc1(a):
#     return a + a

# def calc2(a):
#     return a*a

def math(op, x, y):
    print(op(x, y))

math(lambda a, b: a + b, 5, 45)