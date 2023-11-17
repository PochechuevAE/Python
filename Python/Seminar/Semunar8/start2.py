def calc_power(degree):
    def power(base):
        return base ** degree
    return power

print(calc_power(3) (2))
cube = calc_power(3)
square = calc_power(2)

degrees = [calc_power (i) for i in range(10)]

print(cube(5))
print(square(12))
for i in range(len(degrees)):
    print(degrees[i] (2))
