age = 35
gender = "F"
is_married = True
if gender == "F":
    print("Can work only in city regions")
elif gender == "M" and (20 <= age <= 40):
    print("Can work everywhere")
elif gender == "M" and (41 <= age <= 60):
    print("Can work only in city regions")
elif age < 20 or age > 60:
    print("Error")
