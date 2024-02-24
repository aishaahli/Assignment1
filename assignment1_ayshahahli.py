# -*- coding: utf-8 -*-
"""Assignment1_AyshahAhli

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DONlsTg4qJDHB-cYhCWgvvw9ijaccHoq
"""

#USE CASE 1: generate boarding pass

class Passenger:
    # this line represents a passenger with personal details and a reservation.
    def __init__(self, passportNumber, firstName, lastName, contactNumber, email, reservation):
        self.passportNumber = passportNumber
        self.firstName = firstName
        self.lastName = lastName
        self.contactNumber = contactNumber
        self.email = email
        self.reservation = reservation

class Reservation:
    # this line represents a reservation with details such as number, date, status, and associated flight.
    def __init__(self, reservationNumber, reservationDate, isAvailable, passengerCount, totalPrice, flight):
        self.reservationNumber = reservationNumber
        self.reservationDate = reservationDate
        self.isAvailable = isAvailable
        self.passengerCount = passengerCount
        self.totalPrice = totalPrice
        self.flight = flight

class Flight:
    # this line represents a flight with details like number, cities, times, and availability status.
    def __init__(self, flightNumber, departureCity, arrivalCity, departureTime, arrivalTime, isAvailable):
        self.flightNumber = flightNumber
        self.departureCity = departureCity
        self.arrivalCity = arrivalCity
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        self.isAvailable = isAvailable

class BoardingPass:
    # this line represents a boarding pass with a pass number and details.
    def __init__(self, passNumber, details):
        self.passNumber = passNumber
        self.details = details

class BoardingPassDetails:
    # this line represents details on a boarding pass, including passenger name, seat, gate, etc.
    def __init__(self, passengerName, seatType, gate, date, electronicTicketNumber,
                 time, seatNumber, arrivalCity, arrivalTime, terminalNumber):
        self.passengerName = passengerName
        self.seatType = seatType
        self.gate = gate
        self.date = date
        self.electronicTicketNumber = electronicTicketNumber
        self.time = time
        self.seatNumber = seatNumber
        self.arrivalCity = arrivalCity
        self.arrivalTime = arrivalTime
        self.terminalNumber = terminalNumber

# this line shows additional Placeholder Methods:
class System:
    # this line shows the placeholder method to check flight availability.
    def checkAvailability(self, flight):
        pass

    # this line shows the placeholder method to generate a boarding pass.
    def generateBoardingPass(self, passenger, details):
        pass

# these lines creates objects
passenger_obj = Passenger("UAE667390-3", "Aisha", "Ahli", "0558840444", "aishaahli360@gmail.com", None)
flight_obj = Flight("FL123", "Dubai", "NewYork", "10:00 AM", "12:00 PM", True)
reservation_obj = Reservation("R123", "2024-02-24", True, 1, 150.0, flight_obj)
boarding_pass_details_obj = BoardingPassDetails("Aisha Ahli", "Business", "Gate 1", "2024-02-24", "T123456", "10:00 AM", "A23", "NewYork", "12:00 PM", "Terminal 2")
boarding_pass_obj = BoardingPass("BP123", boarding_pass_details_obj)

# these lines display the boarding pass details
print("Passenger Details:")
print(f"Passport Number: {passenger_obj.passportNumber}")
print(f"Name: {passenger_obj.firstName} {passenger_obj.lastName}")

print("\nReservation Details:")
print(f"Reservation Number: {reservation_obj.reservationNumber}")
print(f"Reservation Date: {reservation_obj.reservationDate}")
print(f"Total Price: ${reservation_obj.totalPrice}")

print("\nFlight Details:")
print(f"Flight Number: {flight_obj.flightNumber}")
print(f"Departure City: {flight_obj.departureCity}")
print(f"Arrival City: {flight_obj.arrivalCity}")

print("\nBoarding Pass Details:")
print(f"Pass Number: {boarding_pass_obj.passNumber}")
print(f"Passenger Name: {boarding_pass_obj.details.passengerName}")
print(f"Seat Type: {boarding_pass_obj.details.seatType}")
print(f"Gate: {boarding_pass_obj.details.gate}")
print(f"Date: {boarding_pass_obj.details.date}")
print(f"Electronic Ticket Number: {boarding_pass_obj.details.electronicTicketNumber}")
print(f"Time: {boarding_pass_obj.details.time}")
print(f"Seat Number: {boarding_pass_obj.details.seatNumber}")
print(f"Arrival City: {boarding_pass_obj.details.arrivalCity}")
print(f"Arrival Time: {boarding_pass_obj.details.arrivalTime}")
print(f"Terminal Number: {boarding_pass_obj.details.terminalNumber}")

#USE CASE 2: cancel reservation

class Passenger:
    # this line represents a passenger with personal details and a reservation.
    def __init__(self, passportNumber, firstName, lastName, contactNumber, email, reservation):
        self.passportNumber = passportNumber
        self.firstName = firstName
        self.lastName = lastName
        self.contactNumber = contactNumber
        self.email = email
        self.reservation = reservation

class Reservation:
    # this line represents a reservation with details such as number, date, status, and associated flight.
    def __init__(self, reservationNumber, reservationDate, status, isRefundable, flight, seatNumber):
        self.reservationNumber = reservationNumber
        self.reservationDate = reservationDate
        self.status = status
        self.isRefundable = isRefundable
        self.flight = flight
        self.seatNumber = seatNumber

class Flight:
    # this line represents a flight with details like number, cities, times, and takeoff status.
    def __init__(self, flightNumber, departureCity, arrivalCity, departureTime, arrivalTime, hasTakenOff):
        self.flightNumber = flightNumber
        self.departureCity = departureCity
        self.arrivalCity = arrivalCity
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        self.hasTakenOff = hasTakenOff

class ReservationStatus:
    # this line represents the status of a reservation with details like ID, description, and activity status.
    def __init__(self, statusID, statusDescription, lastUpdated, createdBy, isActive):
        self.statusID = statusID
        self.statusDescription = statusDescription
        self.lastUpdated = lastUpdated
        self.createdBy = createdBy
        self.isActive = isActive

# this line shows the additional Placeholder Methods:
class System:
    # this line shows the placeholder method to cancel a reservation and update its status.
    def cancelReservation(self, passenger):
        pass

# these lines create objects
passenger_obj = Passenger("UAE48364-4", "Sara", "Alkhoori", "9876543210", "saraalkhoori83@gmail.com", None)
flight_obj = Flight("FL456", "Abudhabi", "Doha", "02:00 PM", "04:00 PM", False)
reservation_status_obj = ReservationStatus(1, "Confirmed", "2024-02-28", "System", True)
reservation_obj = Reservation("R456", "2024-02-15", reservation_status_obj, False, flight_obj, "B15")

# these lines diaplsy the boarding pass details before cancellation
print("Boarding Pass Details Before Cancellation:")
print(f"Passenger Name: {passenger_obj.firstName} {passenger_obj.lastName}")
print(f"Flight Number: {flight_obj.flightNumber}")
print(f"Seat Number: {reservation_obj.seatNumber}")
print(f"Status: {reservation_obj.status.statusDescription}")

# this line displays the cancellation confirmation
print("Before Cancellation:")
print(f"Reservation Status: {reservation_obj.status.statusDescription}")

# this line cancels the reservation
system_obj = System()
system_obj.cancelReservation(passenger_obj)

# this line displays the cancellation confirmation
print("\nAfter Cancellation:")
if reservation_obj.status.isActive:
    print("Cancellation Confirmed")
else:
    print(f"Reservation Status: {reservation_obj.status.statusDescription}")

#USE CASE 3: change seat place

class Passenger:
    # this line represents a passenger with personal details and a reservation.
    def __init__(self, passportNumber, firstName, lastName, contactNumber, email, reservation):
        self.passportNumber = passportNumber
        self.firstName = firstName
        self.lastName = lastName
        self.contactNumber = contactNumber
        self.email = email
        self.reservation = reservation

class Reservation:
    # this line represents a reservation with details such as number, date, status, and associated flight.
    def __init__(self, reservationNumber, reservationDate, status, flight, seatNumber):
        self.reservationNumber = reservationNumber
        self.reservationDate = reservationDate
        self.status = status
        self.flight = flight
        self.seatNumber = seatNumber

class Flight:
    # this line represents a flight with details like number, cities, times, and available seats.
    def __init__(self, flightNumber, departureCity, arrivalCity, departureTime, arrivalTime, availableSeats):
        self.flightNumber = flightNumber
        self.departureCity = departureCity
        self.arrivalCity = arrivalCity
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        self.availableSeats = availableSeats

class ReservationStatus:
    # this line represents the status of a reservation with details like ID, description, and activity status.
    def __init__(self, statusID, statusDescription, lastUpdated, createdBy, isActive):
        self.statusID = statusID
        self.statusDescription = statusDescription
        self.lastUpdated = lastUpdated
        self.createdBy = createdBy
        self.isActive = isActive

# this line shows the additional Placeholder Methods:
class System:
    # this line shows the placeholder method to check flight status and available seats.
    def checkFlightStatus(self, reservation):
        pass

    # this line shows the placeholder method to change the seat for a reservation and return a new boarding pass.
    def changeSeat(self, reservation, newSeat):
        reservation.seatNumber = newSeat

# these lines creates objects
passenger_obj = Passenger("UAE4746-6", "Ahmad", "Younis", "5551112222", "ahmadyounis47@hotmail.com", None)
flight_obj = Flight("FL789", "Dubai", "Poland", "08:00 AM", "10:00 AM", True)
reservation_status_obj = ReservationStatus(1, "Confirmed", "2024-03-10", "System", True)
reservation_obj = Reservation("R789", "2024-03-01", reservation_status_obj, flight_obj, "C12")

# these lines disply the current seat information
print("Before Seat Change:")
print(f"Current Seat Number: {reservation_obj.seatNumber}")

# Changing seat
system_obj = System()
new_seat = "D23"
system_obj.changeSeat(reservation_obj, new_seat)

# these lines display the updated seat information
print("\nAfter Seat Change:")
print(f"Updated Seat Number: {reservation_obj.seatNumber}")

