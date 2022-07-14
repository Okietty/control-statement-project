
#Pattern 1
print("Pattern 1")


for i in range(5):
    if i % 2 == 0:
        print("##########")
        print("##########")
    else:
        print("###")
        print("###")


#Pattern 2
print("Pattern 2")


rowsOfShape = int(input("How many rows should there be (Type 9 for the shape asked for in the instructions): "))
tag = '#'
rowAmount = rowsOfShape/2

for i in range(round(rowAmount + 0.5)):
    print(tag)
    tag += '#'

for i in range(round(rowAmount + 0.5) - 1):
    tag = '#'
    for j in range(round(rowAmount + 0.5) - 2):
        tag += '#'
    print(tag)
    rowAmount -= 1


#Pattern 3
print("Pattern 3")


spacing = 5
print("#######")
for i in range(spacing):
    for j in range(spacing):
        print('' , end =' ')
    print('#')
    spacing -= 1

print("#######")
