from driver import Driver
from passenger import Passenger
from route import Route
from bus import Bus

def main():
    # Create drivers
    d1 = Driver("Sai", "D001", "LIC123")
    d2 = Driver("Tom", "D002", "LIC456")

    # Create routes
    r1 = Route("R101", "City Center", "Airport", ["Station", "Mall", "Highway"])
    r2 = Route("R102", "Downtown", "University", ["Park", "Hospital"])

    # Create buses
    b1 = Bus("B001", 3)
    b2 = Bus("B002", 2)

    # Assign drivers and routes
    b1.assign_driver(d1)
    b1.assign_route(r1)
    b2.assign_driver(d2)
    b2.assign_route(r2)

    # Create passengers
    p1 = Passenger("Neethu", "T001", "Airport")
    p2 = Passenger("Vinitha", "T002", "Mall")
    p3 = Passenger("Pandeti", "T003", "Station")
    p4 = Passenger("Jerry", "T004", "University")

    # Add passengers to Bus 1
    b1.add_passenger(p1)
    b1.add_passenger(p2)
    b1.add_passenger(p3)
    b1.add_passenger(p4)  # Should fail (capacity full)

    # Add passengers to Bus 2
    b2.add_passenger(p4)

    # Start trips
    b1.start_trip()
    b2.start_trip()

    # Remove passenger from Bus 1
    b1.remove_passenger("T002")

    # Display bus status
    print("\n--- Current Bus Status ---")
    b1.display_status()
    b2.display_status()

    # End trips
    b1.end_trip()
    b2.end_trip()

    # Final status after trips
    print("\n--- Final Bus Status ---")
    b1.display_status()
    b2.display_status()

if __name__ == "__main__":
    main()
