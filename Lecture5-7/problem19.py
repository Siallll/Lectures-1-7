text = "Bananas"
words = text.split()
for word in words:  # index is a word in the words
    if len(word) % 2 == 0:  # calculation to find evens
        print(word, end=" ")    # prints the word of evens in right way
    else:
        print(word[::-1], end=" ")  # prints the word of odd in reversed way
print()