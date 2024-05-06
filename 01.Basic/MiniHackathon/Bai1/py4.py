dish = ["Pho","Bun Bo"]

def get_order():
    current_order = []
    while True:
        order = input("Please choose a dish:")
        if order in dish:
            current_order.append(order)
        else:
            print("I'm sorry, we don't serve that.")
            continue
        if is_order_complete():
            return current_order

def is_order_complete():
    choice = input("Great choice! Anything else? (y/n):")
    if choice == "n":
        return True
    elif choice == "y":
        return False
    else:
        print("invalid input")

def output_order(order_list):
    print("Well done! Your order:")
    for order in order_list:
        print(order)

def main():
    order = get_order()
    output_order(order)

if __name__ == "__main__":
    main()

