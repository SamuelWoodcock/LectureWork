age = int(input("Enter age: "))

while age < 0 or age > 120:  # the input is bad
    print("Invalid age")
    age = int(input("Enter age: "))
    if 0 <= age <= 4:
        age_category = 'baby'
    elif 4 < age <= 17:
        age_category = 'child'
    elif 17 < age <= 65:
        age_category = 'adult'
    else:
        age_category = 'elder'
print(f"Your age is {age_category}")


