a = None
b = None

a = input("Enter the weight in kilograms: ")
b = input("Enter your height in meters, e.g. 1.74: ")
b = b.replace(',', '.')
print(int(a) / (float(b) ** 2))