from user import User

class PremiumUser(User):
    DISCOUNT = 0.10  # 10% discount

    def calculate_total(self):
        total = self.cart.calculate_total()
        discounted_total = total * (1 - PremiumUser.DISCOUNT)
        print(f"{self.name}'s cart total with discount: ${discounted_total}")
        return discounted_total
