from cart import Cart

class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def add_to_cart(self, product, quantity):
        self.cart.add_product(product, quantity)

    def remove_from_cart(self, product, quantity):
        self.cart.remove_product(product, quantity)

    def view_cart(self):
        print(f"\n{self.name}'s Cart:")
        self.cart.view_cart()

    def calculate_total(self):
        total = self.cart.calculate_total()
        print(f"{self.name}'s cart total: ${total}")
        return total
