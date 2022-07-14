
#Task 1
print("Task 1")


numForMultiTable = int(input("Choose a number to create a multiplication table for: "))

for i in range(26):
    print(i, "x", numForMultiTable, "=", i*numForMultiTable)


#Task 2
print("Task 2")


x = 1
userNum = int(input("What is your starting number: "))

if userNum == 0:
    print(x)
elif userNum % 2 == 0:
    if userNum < 0:
        x += userNum
        print(x)
    elif userNum > 0:
        x *= userNum
        print(x)
elif userNum % 2 == 1:
    if userNum < 0:
        x -= userNum
        print(x)
    elif userNum > 0:
        x /= userNum
        print(x)