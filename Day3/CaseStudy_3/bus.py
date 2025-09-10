from driver import Driver
from passenger import Passenger
from route import Route

class Bus:
    def __init__(self, bus_no, capacity):
        self.__bus_no = bus_no
        self.__capacity = capacity
        self.__driver = None
        self.__route = None
        self.__passengers = []  # private list

    # Assign driver
    def assign_driver(self, driver: Driver):
        self.__driver = driver
        print(f"Driver '{driver.get_name()}' assigned to Bus {self.__bus_no}.")

    # Assign route
    def assign_route(self, route: Route):
        self.__route = route
        print(f"Route '{route.get_route_no()}' assigned to Bus {self.__bus_no}.")

    # Add passenger
    def add_passenger(self, passenger: Passenger):
        if len(self.__passengers) >= self.__capacity:
            print(f"Cannot add passenger '{passenger.get_name()}': Bus {self.__bus_no} is full.")
            return
        self.__passengers.append(passenger)
        print(f"Passenger '{passenger.get_name()}' added to Bus {self.__bus_no}.")

    # Remove passenger by ticket number
    def remove_passenger(self, ticket_no):
        for p in self.__passengers:
            if p.get_ticket_no() == ticket_no:
                self.__passengers.remove(p)
                print(f"Passenger '{p.get_name()}' removed from Bus {self.__bus_no}.")
                return
        print(f"No passenger with ticket number {ticket_no} found on Bus {self.__bus_no}.")

    # Start trip
    def start_trip(self):
        if not self.__driver:
            print(f"Cannot start trip: No driver assigned to Bus {self.__bus_no}.")
            return
        if not self.__route:
            print(f"Cannot start trip: No route assigned to Bus {self.__bus_no}.")
            return

        print(f"\n--- Trip Started ---")
        print(f"Bus {self.__bus_no} driven by {self.__driver.get_name()} on Route {self.__route.get_route_no()}.")
        print(f"Passengers onboard ({len(self.__passengers)}/{self.__capacity}):")
        for p in self.__passengers:
            p.display_passenger()

    # End trip → clear passengers
    def end_trip(self):
        print(f"\nTrip ended for Bus {self.__bus_no}. Clearing all passengers...")
        self.__passengers.clear()

    # Display bus status
    def display_status(self):
        driver_name = self.__driver.get_name() if self.__driver else "No driver"
        route_no = self.__route.get_route_no() if self.__route else "No route"
        print(f"Bus {self.__bus_no} | Driver: {driver_name} | Route: {route_no} | Passengers: {len(self.__passengers)}/{self.__capacity}")
