secret = 6
guess = int(input("Guess a number: "))
while guess != secret:
    print("Incorrect guess. Try again.")
    guess = int(input("Guess a number: "))
print("Correct!")