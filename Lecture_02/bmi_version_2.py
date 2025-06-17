import random
def main ():
    height = random.uniform(1, 2)
    if calculate_bmi(height, 99) < 15:
        print("Not considered overweight")

def calculate_bmi(height, weight):
    return height * weight / (height ** 2)

main()
