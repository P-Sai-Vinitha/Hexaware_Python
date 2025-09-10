from food_item import FoodItem
from user import User
from premium_user import PremiumUser

# Create food items
pizza = FoodItem("Pizza", 250)
burger = FoodItem("Burger", 150)
pasta = FoodItem("Pasta", 200, available=False)
fries = FoodItem("Fries", 100)

# Create users
john = User("Neethu")
emma = PremiumUser("Vinitha")

# neethu's order
john.order.add_item(pizza)
john.order.add_item(burger)
john.order.add_item(pasta)  # unavailable
john.order.display_order()
john.display_total()

print("\n---\n")

# vinitha's order
emma.order.add_item(pizza)
emma.order.add_item(fries)
emma.order.remove_item("Fries")
emma.order.display_order()
emma.display_total()
