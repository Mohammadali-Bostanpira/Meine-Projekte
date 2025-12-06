while True:
    try:
        mp = input("x/y:")
        x, y = mp.split("/")
        x = int(x)
        y = int(y)
        p = round((x / y)*100)
        if p > 100:
            continue
        if p < 0:
            continue
        if p <= 1:
            print("E")
        elif p >= 99:
            print("F")
        else:
            print(f"{p}%")
        break
    except ValueError:
        print("bayad adad bashe")
    except ZeroDivisionError:
        print("y not be 0")
    continue
