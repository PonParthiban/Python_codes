menu = { "pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries":  2.50,
        "chips": 1.00,
        "soda": 3.00,
        "lemonade": 4.00}
cart = []
total = 0
print("-------------------------------MENU----------------------------------------------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}")
print("----------------------------------------------------------------------------------")
while True:
    items = input("Enter the item to buy(q to quit): ").lower()
    if items == "q":
        break
    elif menu.get(items) is not None:
        cart.append(items)
    else:
        print("check the name of the food")
print("-------------Your Order----------------")
for items in cart:
    total += menu.get(items)
    print(items, end=" ")
    print()

print(f"Total:${total}")
print("------------------------------------------")