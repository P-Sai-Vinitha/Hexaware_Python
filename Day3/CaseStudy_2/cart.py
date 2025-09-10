from product import Product

class Cart:
    def __init__(self):
        self.items = {}  # {product: quantity}
        self.last_added_item = None  # Dynamic attribute

    # Add product to cart
    def add_product(self, product: Product, quantity):
        if product.get_stock() < quantity:
            print(f"Not enough stock for '{product.get_name()}'. Available: {product.get_stock()}")
            return

        # Reduce stock
        product.reduce_stock(quantity)

        # Add to cart
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

        # Dynamic attribute
        self.last_added_item = product.get_name()

        print(f"Added '{product.get_name()}' x{quantity} to cart.")

    # Remove product from cart
    def remove_product(self, product: Product, quantity):
        if product not in self.items:
            print(f"'{product.get_name()}' is not in the cart.")
            return

        if quantity >= self.items[product]:
            # Remove completely
            removed_qty = self.items.pop(product)
            product.increase_stock(removed_qty)
        else:
            self.items[product] -= quantity
            product.increase_stock(quantity)

        print(f"Removed '{product.get_name()}' x{quantity} from cart.")

    # View cart items
    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
            return

        print("\nItems in Cart:")
        for product, qty in self.items.items():
            print(f"{product.get_name()} x{qty} = ${product.get_price() * qty}")

    # Calculate total cost (to be overridden by PremiumUser if needed)
    def calculate_total(self):
        total = sum(product.get_price() * qty for product, qty in self.items.items())
        return total
