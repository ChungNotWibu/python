n = int(input("Number of items: "))
menu = []
for i in range(n):
    item = input(f"Item {i+1}: ")
    price = float(input(f"Price of item {i+1}: "))
    menu.append((item, price))

average_price = sum([item[1] for item in menu])/n
print(f"Average price: {average_price:.2f}")

above_average_items = [item for item in menu if item[1] > average_price]
print("Item(s) above average price:", *above_average_items)