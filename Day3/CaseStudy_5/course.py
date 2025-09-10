class Course:
    def __init__(self, name, code, credits, fee):
        self.name = name
        self.code = code
        self.credits = credits
        self.__fee = fee  # Encapsulation - private attribute

    def get_fee(self):
        return self.__fee

    def display(self):
        print(f"Course: {self.name} ({self.code}), Credits: {self.credits}, Fee: ₹{self.__fee}")
