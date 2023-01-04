user_input = "Hello world!"
sum = 0
for char in {*user_input}:  # removing all duplicates
    symbol_count = user_input.count(char)  # counting how many times 1 variable is found
    if symbol_count > 1:  # if symbols found are more than 1
        sum += symbol_count - 1  # removing 1 original symbol
print(sum)
