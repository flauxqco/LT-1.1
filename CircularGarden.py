import math

radius = float(input("Enter radius: "))
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * (radius)
square = math.sqrt(area)
down = math.floor(area)
up = math.ceil(area)

print(f"Area of the garden: {area:.2f} square meters")
print(f"Circumference of the garden: {circumference:.2f} meters")
print(f"Square root of the area: {square:.2f}")
print(f"Area rounded down: {down:.2f} meters")
print(f"Area rounded up: {up:.2f} meters")
