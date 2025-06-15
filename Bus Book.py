#Bus Booking Platform

class Bus:
    def __init__(self, bus_id, bus_name, seats_available, fare):
        self.bus_id = bus_id
        self.bus_name = bus_name
        self.seats_available = seats_available
    def book_seat(self, passenger_name):
        if self.seats_available > 0:
            self.seats_available -= 1
            print(f"{passenger_name} has successfully booked a seat on bus {self.bus_id}. Remaining seats: {self.seats_available}")
        else:
            print(f"Sorry, bus {self.bus_id} is fully booked.")
    def cancel_booking(self, passenger_name):
        if self.seats_available < self.bus_seats:
            self.seats_available += 1
            print(f"{passenger_name} has successfully cancelled their booking on bus {self.bus_id}. Remaining seats: {self.seats_available}")
        