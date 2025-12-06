s = input("voroodi:")
vowels = ("a", "e", "o", "i", "u", "A", "E", "O", "I", "U")
for c in s:
    if c not in vowels:
        print(c, end="")
        