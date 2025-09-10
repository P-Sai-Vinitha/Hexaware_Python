from product import Product
from user import User
from premium_user import PremiumUser

def main():
    # Create products
    laptop = Product("Laptop", 1000, 5)
    mouse = Product("Mouse", 50, 10)
    keyboard = Product("Keyboard", 80, 7)

    # Display all products
    print("\nAvailable Products:")
    laptop.display_info()
    mouse.display_info()
    keyboard.display_info()

    # Create users
    alice = User("Neethu")
    bob = PremiumUser("Vinitha")

    # Alice adds products to cart
    alice.add_to_cart(laptop, 1)
    alice.add_to_cart(mouse, 2)
    alice.view_cart()
    alice.calculate_total()

    # Bob adds products to cart (premium discount applies)
    bob.add_to_cart(laptop, 1)
    bob.add_to_cart(keyboard, 1)
    bob.view_cart()
    bob.calculate_total()

    # Alice removes a product
    alice.remove_from_cart(mouse, 1)
    alice.view_cart()
    alice.calculate_total()

    # Final stock display
    print("\nFinal Stock Status:")
    laptop.display_info()
    mouse.display_info()
    keyboard.display_info()

if __name__ == "__main__":
    main()
