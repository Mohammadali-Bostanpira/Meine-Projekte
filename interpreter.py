expression = input("expression:")
x, y, z = expression.split(" ")

x = float(x)
z = float(z)


if y == "+":
    print(x+z)

elif y == "-":
    print(x-z)

elif y == "*":
    print(x*z)

elif y == "/" and x > z:
    if z != 0:
        print(x/z)
    else:
        print("mojaz nist")
