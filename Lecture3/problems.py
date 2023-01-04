num = 23
real_num = 4.5
is_logged = False
name = "John"
print("{} {} {} {}".format(num, real_num, is_logged, name))
print(f"{num} {real_num} {is_logged} {name}")

paragraph = "Python is a great language!\", said Fred. \"I Don't ever remember having this much fun before."
print(paragraph)
# Problem 1
country = "usa"
correct_country = country.upper()
print(correct_country)
# Problem 2
filename = "hello.py"
print(filename.endswith(".java"))
print(filename.find("py"))
print(filename.startswith("world"))
print(filename.strip(".py"))
print(filename[0:5])
print(filename[:filename.find(".py")])  # how to combine more functions
# Problem 3
name = "$$John Smith"
print(name.strip("$"))
print(name[2:])
print(name.replace("$", ""))
# Problem 4
width = 60
header = "Coding Temple, Inc"
num_of_intervals = (width - len(header)) // 2
print("*" * width)
print("Coding Temple, Inc".center(width))
print(f"{' ' * num_of_intervals}283 Franklin St.")
print(f"{' ' * num_of_intervals}Boston, MA")
print("=" * width)
num_intervals = 20
product = "Product Name".ljust(num_intervals, ' ')
product_price = "Product Price".ljust(num_intervals, ' ')
print((product + product_price).center(width))
books = "Books".ljust(num_intervals, ' ')
price_books = "$49.95".ljust(num_intervals, ' ')
print((books + price_books).center(width))
computer = "Computer".ljust(num_intervals, ' ')
computer_price = "$579.99".ljust(num_intervals, ' ')
print((computer + computer_price).center(width))
monitor = "Monitor".ljust(num_intervals, ' ')
monitor_price = "$124.89".ljust(num_intervals, ' ')
print((monitor + monitor_price).center(width))
print("=" * width)
print(f"{' ' * 30}{'Total'}")
print(f"{' ' * 30}{'$754.83'}")
print("=" * width)
print("Thanks for shopping with us today!".center(width))
print("*" * width)
