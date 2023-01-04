comment = """Text
here
and
here"""  # This is a multiline string, keeps the format of the string
print(comment)

# text="Text' gets error

name = "matt"
print(name, id(name))  # Prints the id of name
correct = name.capitalize()
print(correct, id(correct))  # Capitalize and show id of correct

name = "John"
last_name = "Smith"
full_name = "John" + " " + last_name  # Concatenation
print(full_name)

first_name = "John"
last_name = "Smith"
full_name = "My full name is {} {}".format(first_name, last_name)  # Format a string with .format
print(full_name)
print(f"My full name is {first_name} {last_name}")  # Format with (f) preferable

print("String:%s" % first_name)  # String format with %s
num = 5
print("Integer:%d" % num)  # Integer format with %d
real_num = 5.4
print("Real number:%f" % real_num)  # Real number format with %f

print("My full name is %s %s" % (first_name, last_name))
num = 5.234234
print("%.2f" % num)  # Limits the symbols behind the . (2 symbols)
print("{:.2f}".format(num))
print(f"{num:.2f}")

# using indexes to print each element
string = "foobar"
print(string[0])  # prints f, the index is 0 (Get first element)
print(string[1])  # prints o, the index is 1 (Get second element)
print(string[-1])  # prints r, the index is -1 (Get last element)
# print(string[20]) # Error index out of range

# slicing ,syntax is variable_name[start:stop:step]
word = "Hello"
print(word[0:5:2])  # output will be "Hlo" (first element, sixth element, step 2)
print(word[0:3])  # output will be "Hel" (from first to third element)
print(word[-6:-1])  # slice with negative indices
print(word[-1:-6:-1])  # reverse - slice with negative indices and step
name = "John Smith"
last_name = name[5:-1]  # Slice with a positive and a negative index
print(last_name)
print(name[:5])  # Slice from start to 4th
print(name[5:])  # Slice from start to last
print(name[::])  # Slice over the whole str
print(name[::-1])  # Reverse a string
print(name[50:80])  # empty string

# .title()
name = "john smith"
print(name)
print(name.title())  # Titles the string without saving it
name = name.title()  # Titles the string and saves in the ram
print(name)

# .replace()
word = "Hello there!"
print(word.replace("!", '.'))  # Replace ! with .
print(word)

# .find()
print(word.find("l"))
comma_index = word.find(" ")  # Variable on space
print(word[comma_index + 1:])  # print from space to end
# comma_index = word.find("@")  # Find a missing value

# .strip()
name = "   Ivan"
print(name.strip())  # remove of spaces, tabs, newlines
name = "@@@@@Ivan"
print(name.strip("@"))  # removes @
name = "@Ivan@"
print(name.lstrip("@"))  # Strip on left side
print(name.rstrip("@"))  # Strip on right side

# len
print(len("Hello, world"))  # Show length of string
# in
name = "@Ivan"
print("@" in name)

# .split()
word = "Hello, world"
print(word.split())  # Split a string

# .startswith()
word2 = "Hello, world!"
print(word2.startswith("H"))  # how string starts with
# .endswith()
print(word2.endswith("!"))  # how string ends with

