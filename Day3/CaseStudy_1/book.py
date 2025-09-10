class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__available = True  # private attribute

    # Getters
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def is_available(self):
        return self.__available

    # Setter for availability
    def set_availability(self, status):
        self.__available = status

    def display_info(self):
        status = "Available" if self.__available else "Borrowed"
        print(f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, Status: {status}")
