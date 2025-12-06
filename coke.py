price = 50
while price > 0:
    coin = int(input("Insert Coin:"))

    if coin in [5, 10, 25]:
        price = price - coin
        print(f"Amount Due: {price}")
    else:
        print("Amount Due: 50")


change = abs(price)
print(f"Change Owed: {change}")
