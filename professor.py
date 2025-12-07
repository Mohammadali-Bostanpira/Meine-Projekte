import random


def main():
    level = get_level()
    Score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        add = x + y

        talash = 0
        while True:
            try:
                javab = int(input(f"{x} + {y} = "))
                if javab == add:
                    Score += 1
                    break
                else:
                    print("EEE")
                    talash += 1
                    if talash == 3:
                        print(add)
                        break

            except ValueError:
                print("EEE")
                talash += 1
                if talash == 3:
                    print(add)
                    break
    print(f"Score: {Score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
