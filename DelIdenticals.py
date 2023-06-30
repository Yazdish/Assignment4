Array_1 = []
x = input("enter sequence: ")
y = x.split(",")
for i in range(len(y)):
    y[i] = int(y[i])

for i in range(len(y)):
    for j in range(i+1, len(y)-1):
        if y[i] == y[j]:
            y.pop(j)
        else:
            j += 1
    i +=1
print(y)