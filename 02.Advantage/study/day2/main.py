# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def add(self,point):
#         new_x = self.x + point.x
#         new_y = self.y + point.y
#         return Point(new_x,new_y)
#     def sub(self,point):
#         new_x = self.x - point.x
#         new_y = self.y - point.y
#         return Point(new_x,new_y)

# point1 = Point(2,3)
# point2 = Point(4,5)

# result_add = point1.add(point2)
# print(f"Tọa độ kết quả phép cộng 2 điểm là :({result_add.x},{result_add.y})")
# result_add = point1.sub(point2)
# print(f"Tọa độ kết quả phép trừ 2 điểm là :({result_add.x},{result_add.y})")


# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def display_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}")


# class Car(Vehicle):
#     def __init__(self, brand, model, num_doors):
#         super().__init__(brand, model)
#         self.num_doors = num_doors

#     def display_info(self):
#         super().display_info()
#         print(f"Number of Doors: {self.num_doors}")


# class Motorcycle(Vehicle):
#     def __init__(self, brand, model, has_sidecar):
#         super().__init__(brand, model)
#         self.has_sidecar = has_sidecar

#     def display_info(self):
#         super().display_info()
#         sidecar_info = "Yes" if self.has_sidecar else "No"
#         print(f"Has Sidecar: {sidecar_info}")



# car_obj = Car("Toyota", "Camry", 4)
# motorcycle_obj = Motorcycle("Harley-Davidson", "Sportster", True)


# print("Car Information:")
# car_obj.display_info()  

# print("\nMotorcycle Information:")
# motorcycle_obj.display_info()

class Product:
    def __init__(self, product_id, name, price, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def calculate_total_cost(self, quantity):
        return self.price * quantity
    

class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []
        self.total_amount = 0

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})
        self.calculate_total_amount()

    def remove_item(self, product):
        self.items = [item for item in self.items if item["product"] != product]
        self.calculate_total_amount()

    def calculate_total_amount(self):
        self.total_amount = sum(item["product"].calculate_total_cost(item["quantity"]) for item in self.items)


class Customer:
    def __init__(self, customer_id, name, address):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)

    def cancel_order(self, order):
        self.orders.remove(order)

    def display_orders(self):
        for order in self.orders:
            print(f"Order ID: {order.order_id}. Total Amount: {order.total_amount}")


# Tạo sản phẩm
product1 = Product("P001", "Áo thun", 15.99, 50)
product2 = Product("P002", "Quần jean", 29.99, 30)
product3 = Product("P003", "Giày thể thao", 49.99, 20)

# Tạo đơn hàng
order1 = Order("O 001")
order2 = Order("O 002")

# Khách hàng
customer = Customer("C001", "Nguyễn Văn A", "123 Đường ABC")

# Thêm sản phẩm vào đơn hàng
order1.add_item(product1, 2)
order1.add_item(product2, 1)
order2.add_item(product2, 3)
order2.add_item(product3, 2)

# Đặt đơn hàng cho khách hàng
customer.place_order(order1)
customer.place_order(order2)

# Hiển thị thông tin đơn hàng của khách hàng
customer.display_orders()