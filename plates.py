def main():
    plate = input("Plate: ")
    print("Valid" if is_valid(plate) else "Invalid")


def is_valid(s):

    if not (2 <= len(s) <= 6):
        return False


    if not s[:2].isalpha():
        return False

    number_started = False

    for c in s:

        if not c.isalnum():
            return False

        if c.isdigit():

            if not number_started:
                if c == '0':
                    return False
                number_started = True

        else: 

            if number_started:
                return False

    return True


if __name__ == "__main__":
    main()
