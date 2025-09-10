class Driver:
    def __init__(self, name, emp_id, license_no):
        self.__name = name
        self.__emp_id = emp_id
        self.__license_no = license_no

    # Getters
    def get_name(self):
        return self.__name

    def get_emp_id(self):
        return self.__emp_id

    def get_license_no(self):
        return self.__license_no

    # Display driver details
    def display_driver(self):
        print(f"Driver: {self.__name}, Employee ID: {self.__emp_id}, License: {self.__license_no}")
