Array_1 = []
x = input("enter sequence: ")
y = x.split(",")
for i in range(len(y)):
    y[i] = int(y[i])
y = y.reverse()
print(y)
