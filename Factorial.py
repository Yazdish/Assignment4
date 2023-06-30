Num = int(input("pls enter number: "))
IsFac = False
i = 1
while i < Num: 
    if Num % i == 0:
        Num = Num/i
        i += 1
        IsFac = True
    else:
        IsFac = False
        break
if IsFac == True:
    print("YES")
else:
    print("NO")
