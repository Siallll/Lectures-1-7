for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

#    print(*("*" * i), sep=" ") simpler syntax for advanced coding
for i in range(6, 0, -1):
    print(*("*" * i), sep=" ")
