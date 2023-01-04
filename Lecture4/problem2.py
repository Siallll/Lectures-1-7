a, b = 5, 3
if a > 0 and b > 0 or a < 0 and b < 0:
    print('+')
elif (a < 0 and b > 0) or (a > 0 and b < 0):
    print('-')
else:
    print("cannot divide by zero")
