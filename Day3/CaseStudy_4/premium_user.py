from user import User

class PremiumUser(User):
    def __init__(self, name):
        super().__init__(name)

    def calculate_total(self):
        total = super().calculate_total()
        return total * 0.85  # 15% discount

    def display_total(self):
        total = self.calculate_total()
        print(f"{self.name}'s order total with discount: ₹{total}")
