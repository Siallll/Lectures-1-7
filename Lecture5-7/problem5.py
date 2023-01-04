numbers = "1,2,3,4,5,6,7,8,9"
odd = 0
even = 0
for text in numbers.split(","):
    num = int(text)
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Odds={odd}, Evens={even}")