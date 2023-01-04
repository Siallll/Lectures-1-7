user_input = int(input())
# for i in range(1, user_input):
#    if 1 <= i <= 9:
#        print(i, end="-")
#    else:
#        print(str(i)[0], str(i)[1], sep="-", end="-")
# if 1 <= user_input <= 9:
#    print(user_input)
# else:
#    print(str(user_input)[0], str(user_input)[1], sep="-")
# Solve for numbers up to 99
# for i in range(1, user_input):
#    if 1 <= i <= 9:
#        print(i, end="-")
#    else:
#        for char in str(i):
#            print(char, end="-")
# if 1 <= user_input <= 9:
#    print(user_input)
# else:
#    for char in str(user_input)[:-1]:
#        print(char, end="-")
#    print(str(user_input)[-1])
# Solve for numbers above 99
text = ""
for num in range(1, user_input + 1):
    text += str(num)
print("-".join(text))  # Best and small solution

