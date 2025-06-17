ages = []
total_age = 0
n = 0
age= 0
#PROMPT for the first age input


#LOOP UNTIL USER ENTERS -1
while age != -1:
    age = int(input("Enter age(-1 to Exit Program): "))
    if age == -1:
        break
    elif age < 0 or age < 120:
        print(f'Please enter a age between 0 and 120')
    else:
        ages.append(age)
        total_age += age
        n += 1

        average_age = total_age / n
if n > 0:
        print(f"Average age: {average_age}")
        print(F"Total age: {total_age}")