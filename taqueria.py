menu = {
        "baja taco": 4.00,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.75,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00
        }

total = 0
while True:
    try:
        key = input("Item: ")
        key = key.lower().strip()

        if key in menu:
            n = menu[key]
            total += float(n)
            print(f"${total:.2f}")
            continue

        else:
            continue

    except EOFError:
        print("barname tamam")
    break
