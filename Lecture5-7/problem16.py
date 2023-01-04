user_input = "aaabbbccc"
found = ""
for char in user_input:
    if char not in found:
        print(char, end=" ")
    found += char
