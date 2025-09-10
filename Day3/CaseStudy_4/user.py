from order import Order

class User:
    def __init__(self, name):
        self.name = name
        self.order = Order()

    def calculate_total(self):
        return self.order.calculate_total()

    def display_total(self):
        total = self.calculate_total()
        print(f"{self.name}'s order total: ₹{total}")
