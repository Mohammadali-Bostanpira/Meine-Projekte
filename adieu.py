import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input()
    except EOFError:
        break
    if name == "":
        break
    names.append(name)


print("Adieu, adieu, to", p.join(names))
