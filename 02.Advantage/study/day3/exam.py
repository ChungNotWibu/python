class Product:
    def __init__(self, name, price, product_type):
        self.name = name
        self.price = price
        self.product_type = product_type

class ConsumerProduct(Product):
    def __init__(self, name, price, product_type, expiration_date):
        super().__init__(name, price, product_type)
        self.expiration_date = expiration_date

class ElectronicProduct(Product):
    def __init__(self, name, price, product_type, warranty_period):
        super().__init__(name, price, product_type)
        self.warranty_period = warranty_period

class FashionProduct(Product):
    def __init__(self, name, price, product_type, size):
        super().__init__(name, price, product_type)
        self.size = size

class ProductManager:
    def __init__(self):
        self.products = []
   
    def add_product(self, product):
        self.products.append(product)
  
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
   
    def update_product(self, product):
        for i, p in enumerate(self.products):
            if p.name == product.name:
                self.products[i] = product
                break
    def find_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def sort_products(self, sort_by):
        self.products.sort(key=lambda x: getattr(x, sort_by))

    def filter_products(self, filter_by):
        return [product for product in self.products if getattr(product, filter_by)]

    def count_products(self, product_type):
        return sum(1 for product in self.products if isinstance(product, product_type))

product_manager = ProductManager()

product_1 = ConsumerProduct("Sữa tươi", 10000, "Hàng tiêu dùng", "2023-08-01")
product_manager.add_product(product_1)

product_2 = ElectronicProduct("Máy tính", 2000000, "Hàng điện tử", 12)
product_manager.add_product(product_2)

product_3 = FashionProduct("Áo sơ mi", 500000, "Hàng thời trang", "M")
product_manager.add_product(product_3)

product = product_manager.find_product("Sữa tươi")
print(product.name, product.price, product.product_type, product.expiration_date)

product_manager.remove_product(product_2)
print(product_manager.products)
