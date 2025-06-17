
n = int(input("How many people are in the room:"))

total_age = 0
ages = []
if   0 >= n:
    print("Invalid input")

for i in range(n):
    age = int(input(f"Enter the age of the person{i+1}:"))
    if age < 0:
        print('Invalid input')
    ages.append(age)
    total_age += age
    average_age = total_age / n


    print(f" Total age: {total_age}")

if n == n:
    print(f"Average age: {average_age}")

