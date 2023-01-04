print("Iskren")

x = 3
name = "Iskren"
y = 4.3
is_loged_in = True
print(type(x), type(name), type(y), type(is_loged_in), sep="\n")

x = 3
y = 10
result = x * y
print(x, "+", y, "=", result)

h = 13.66
l = 245.54
area = ((h * l) / 2)
print(area)

first_name = "Ivan"
last_name = "Ivanov"
age = 34
gender = "M"
identification_num = 27560154
print(first_name, last_name)
print(age, gender, identification_num)

e = 5
f = 10
print("f=", e, " e=", f, sep="")

e, f = f, e  # Multiple switch on one line of code
print("f=", f, " e=", e, sep="")  # Preferred switch

x = int(input())
y = int(input())
area = x * y
perimeter = x * 2 + y * 2
print("Area=", area)
print("Perimeter=", perimeter)
