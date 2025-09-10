from student import Student

class PremiumStudent(Student):
    def __init__(self, name):
        super().__init__(name)

    def calculate_fees(self):
        total = super().calculate_fees()
        return total * 0.8  # 20% discount

    def display_totals(self):
        credits = self.enrollment.calculate_total_credits()
        fees = self.calculate_fees()
        print(f"{self.name}'s total credits: {credits}, Fees with discount: ₹{fees}")
