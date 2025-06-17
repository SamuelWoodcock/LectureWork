import random

length = int(input("Length of rectangle:  "))
width = random.randint(1, length)

area = length * width
print(f"The area of the rectangle {length} x {width} is {area}")

