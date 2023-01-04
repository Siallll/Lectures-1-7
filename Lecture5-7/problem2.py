sum = 0
i = 0
while i < 5:
    user_input = input()
    try:
        int(user_input)
    except ValueError:
        print("Not a number")
        continue
    if int(user_input) < 0 or int(user_input) > 5555:
        print("Number out of range 0-5555")
        continue
    sum += int(user_input)
    i += 1
print(sum)
