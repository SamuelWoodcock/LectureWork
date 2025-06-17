import random

low = int(input("Lower limit: "))
high = int(input("Upper limit: "))
secret = random.randint(low, high)
guess = int(input("Guess a number: "))
while guess != secret:
    print("Incorrect guess. Try again.")
    guess = int(input("Guess a number: "))
print("Correct!")