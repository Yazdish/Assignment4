userList = []
Reversed = []

while True:
    user_input = input("enter number/word or E to Exit: ")
    if user_input == "E":
        break
    else:
        userList.append(user_input)
for i in range(len(userList),0, -1):
    Reversed.append(userList[i-1])
print(Reversed)
