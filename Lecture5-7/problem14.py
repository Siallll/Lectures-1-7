import random

hidden_number = random.randint(0, 100)
while True:
    try:
        num = int(input("Please enter a number from 0 to 100\n"))
        if num == hidden_number:
            print("Exactly right!")
            break
        elif num < hidden_number:
            print("Too low, try again")
        elif num > hidden_number:
            print("Too high, try again!")
    except ValueError:
        print("Invalid input")
print("Thank you for playing!")
