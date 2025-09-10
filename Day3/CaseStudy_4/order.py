class Order:
    def __init__(self):
        self.items = []
        self.last_ordered_item = None  # Dynamic attribute

    def add_item(self, food_item):
        if food_item.available:
            self.items.append(food_item)
            self.last_ordered_item = food_item.name
            print(f"Added '{food_item.name}' to order.")
        else:
            print(f"Sorry, '{food_item.name}' is not available.")

    def remove_item(self, food_item_name):
        for item in self.items:
            if item.name == food_item_name:
                self.items.remove(item)
                print(f"Removed '{food_item_name}' from order.")
                return
        print(f"'{food_item_name}' not found in order.")

    def display_order(self):
        if not self.items:
            print("Your order is empty.")
            return
        print("Your order contains:")
        for item in self.items:
            print(f"- {item.name} (₹{item.price})")
        print(f"Total: ₹{self.calculate_total()}")

    def calculate_total(self):
        return sum(item.price for item in self.items)
