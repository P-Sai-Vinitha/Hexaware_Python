class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    # Getters
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    # Reduce stock when product is added to cart
    def reduce_stock(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
        else:
            raise ValueError("Not enough stock available!")

    # Increase stock when product is removed from cart
    def increase_stock(self, quantity):
        self.__stock += quantity

    def display_info(self):
        print(f"Product: {self.__name}, Price: ${self.__price}, Stock: {self.__stock}")
