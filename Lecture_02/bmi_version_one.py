def main ():
    height = float(input("Enter the height (m): "))
    weight = float(input("Enter the weight (kg): "))
    bmi = calculate_bmi (height, weight)
    print(f"The BMI is {bmi:.2f}")

def calculate_bmi (height, weight):
    return weight / (height ** 2)

main()