#weight_convertion program
weight = int(input("Enter your weight: "))
unit = input("Kilograms or pounds ( K or L): ").upper()
if unit == "K":
    weight = float(weight) * 2.205
    print(f"Your weight is {weight}kg")
elif unit == "L":
    weight = float(weight) / 2.205
    print(f"Your weight is {weight}lb")
else:
    print("Invalid choice!!")