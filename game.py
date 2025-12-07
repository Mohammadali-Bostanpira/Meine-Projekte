import random

while True:
    try:
        level = int(input("Level:"))
        if level > 0 :
            break
    except:
        continue

add = random.randint(1,level)

while True:
    try:
        hads = int(input("Guess:"))
        if hads <= 0:
            continue
    except:
        continue

    if hads < add:
        print("Too small!")
    elif hads > add:
        print("Too large!")
    else:
        print("Just right!")

        break
