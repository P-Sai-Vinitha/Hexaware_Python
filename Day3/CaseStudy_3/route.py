class Route:
    def __init__(self, route_no, start, end, stops=None):
        self.__route_no = route_no
        self.__start = start
        self.__end = end
        self.__stops = stops if stops else []

    # Getters
    def get_route_no(self):
        return self.__route_no

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def get_stops(self):
        return self.__stops

    # Display route details
    def display_route(self):
        print(f"Route {self.__route_no}: {self.__start} → {self.__end}")
        if self.__stops:
            print("Stops:", " → ".join(self.__stops))
