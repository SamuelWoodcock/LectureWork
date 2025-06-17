def determine_category(age, minor_max=17, adult_max=64):
    if not isinstance(age, (int, float)):
        return "Invalid Input"  # Handle non-numeric input
    if age < 0:
        return "Invalid Input"  # Handle negative age
    if 0 <= age <= minor_max:
        return "Minor"
    elif minor_max < age <= adult_max:
        return "Adult"
    else:
        return "Senior"
for age in range(101):
    category = determine_category(age)
    print(f"{age}: {category}")