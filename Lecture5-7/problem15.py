num = int(input("Please enter a number\n"))
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        print("Not prime")
        break
else:
    print("Is prime")