#input form user
i1 = int(input("Enter the first number: "))
i2 = int(input("Enter the first number: "))
li1 = []
li2 = []
print()
while len(li1)< 10:
    li1.append(i1)
    li2.append(i2)
    i1 += 1
    i2 += 1
i = 0
while i < len(li1):
    print("\t", li1[i], end="")
    i += 1
print("\n")
print("\t", end="")
while i >= 0:
    print("-------",end="")
    i -= 1
print("\n")
num = 0
while num < 10:
    index = 0
    print(li2[num],"|", end="\t")
    while index < 10:
        a = li2[num] * li1[index]
        print(a, end="\t")
        index += 1
    print('\n')
    num += 1
