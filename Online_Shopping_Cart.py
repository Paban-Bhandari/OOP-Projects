"""
4. Online Shopping Cart
User
Product
Cart
Order
Payment

Features:
Add to cart
Remove from cart
Calculate total
Place order
Multiple payment methods
Payment
├── Esewa
├── Khalti
└── BankTransfer

Concepts:

Composition
Polymorphism
Aggregation
"""

class Product:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        self.products.append(product)
        print(f"{product.name} added to cart")

    def remove_product(self,product_id):
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                print(f"{product.name} removed from cart.")
                return
        print("Product not found.")

    def calculate_total(self):
        total = 0
        for product in self.products:
            total+=product.price
        return total

class User:
    def __init__(self,name):
        self.name=name
        self.cart=Cart()

class Payment:
    def process_payment(self, amount):
        pass

class Esewa(Payment):
    def process_payment(self, amount):
        print(f"Processing Payment via Esewa....")
        print(f"Paid Rs. {amount} successfully using Esewa")

class Khalti(Payment):
    def process_payment(self, amount):
        print(f"Processing Payment via Khalti....")
        print(f"Paid Rs. {amount} successfully using Khalti")

class MobileBanking(Payment):
    def process_payment(self, amount):
        print(f"Processing Payment via MobileBanking....")
        print(f"Paid Rs. {amount} successfully using MobileBanking")

class Order:
    def __init__(self, cart):
        self.products = cart.products.copy()
        self.total = cart.calculate_total()
        self.status = "Pending"

    def show_order(self):
        print("\n--- ORDER DETAILS ---")
        for product in self.products:
            print(product.id, product.name, product.price)

        print("Total:", self.total)
        print("Status:", self.status)

    def pay(self, payment_method):
        payment_method.process_payment(self.total)
        self.status = "Paid"
        print("Order status updated to PAID")
    

laptop = Product(1, "Laptop", 80000)
mouse = Product(2, "Mouse", 1500)
keyboard = Product(3, "Keyboard", 3000)

user = User("Paban")

user.cart.add_product(laptop)
user.cart.add_product(mouse)
user.cart.add_product(keyboard)

user.cart.remove_product(2)

order = Order(user.cart)

order.show_order()

payment = Esewa()
order.pay(payment)

order.show_order()