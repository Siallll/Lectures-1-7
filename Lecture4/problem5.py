a, b, c = 3, -3, 6
if a + b == 0:
    print(a, b)
elif a + c == 0:
    print(a, c)
elif b + c == 0:
    print(b, c)
elif a + b + c == 0:
    print(a, b, c)
else:
    print('No sum equal 0')
