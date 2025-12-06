text = input("camelCase:")
for c in text:
    if c.isupper():
        c = "_" + c.lower()
        print(c, end="")
    else:
        print(c, end="")

