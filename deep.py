voroodi = input("voroodi:")
x = voroodi.lower().strip()
if x == '42':
    print("yes")
elif x == 'forty-two':
    print("yes")
elif x == 'forty two':
    print("yes")

else:
    print("No")
