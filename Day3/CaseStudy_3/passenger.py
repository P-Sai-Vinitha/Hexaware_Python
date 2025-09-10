class Passenger:
    def __init__(self, name, ticket_no, destination):
        self.__name = name
        self.__ticket_no = ticket_no
        self.__destination = destination

    # Getters
    def get_name(self):
        return self.__name

    def get_ticket_no(self):
        return self.__ticket_no

    def get_destination(self):
        return self.__destination

    # Display passenger details
    def display_passenger(self):
        print(f"Passenger: {self.__name}, Ticket: {self.__ticket_no}, Destination: {self.__destination}")
