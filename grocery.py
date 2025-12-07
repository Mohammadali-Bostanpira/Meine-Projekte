mp = {}
while True:
    try:
        Item = input()
        Item = Item.upper()

        if Item in mp:
            mp[Item] += 1
        else:
            mp[Item] = 1

        continue

    except EOFError:
        for i in sorted(mp.keys()):
            print(f"{mp[i]} {i}")

    break
