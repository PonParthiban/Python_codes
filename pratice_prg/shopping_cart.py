foods = []
prices = []
total = 0
while True:
 food = input("Enter the food(q to quit): ").lower()
 if food == "q":
    print("Thank you for shopping :)")
    break
 else:
    price = float(input("Enter the price of the food:$ "))
    foods.append(food)
    prices.append(price)

for food in foods:
    print(food)
for price in prices:
    total += price
print(f"Total: ${total}")