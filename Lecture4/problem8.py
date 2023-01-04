a, b, c = 15.0, 15.1, 15.2
if a > b > c:
    print(a, b, c)
elif a > c > b:
    print(a, c, b)
elif b > a > c:
    print(b, a, c)
elif b > c > a:
    print(b, c, a)
elif c > a > b:
    print(c, a, b)
elif c > b > a:
    print(c, b, a)
elif a == b == c:
    print(a, b, c)
elif a == b > c:
    print(a, b, c)
elif a == c > b:
    print(a, c, b)
elif b == c > a:
    print(b, c, a)
elif a == b == c:
    print(a, b, c)
else:
    print("Wrong input")
