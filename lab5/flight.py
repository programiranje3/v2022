#%%
"""
LAB 5, class Flight
"""

"""
Create the Flight class with the following elements:

- class attribute *departure_format* representing the expected format for 
  the departure date and time; its value should be "%Y-%m-%d %H:%M"

- a constructor (__init__()) that receives two input parameters and uses them to initialise 
  *flight_num* (flight number) and *departure* (departure date and time) attributes; 
  it also initialises the *passengers* attribute (a list of objects of the Passenger class) 
  to an empty list

- get and set methods for the *departure* attribute (using appropriate decorators); 
  make this attribute private and assure that it is a datetime object that refers to 
  a moment in the future

- a method for adding a passenger to the *passengers* list; the method adds a new passenger 
  only if the input parameter is of the Passenger class, if the passenger is not already 
  in the list, and if he/she is covid safe

- a method that returns a string representation of the given Flight object (__str__())

- a method that returns the time left till departure as a tuple of the form (days, hours, mins)

- methods for turning the given Flight object into an iterator (__iter__(), __next__()) over the 
  flight passengers (that is, elements of the *passengers* list)

"""

#%%
from datetime import datetime
from lab5.passenger import Passenger


class Flight:

    departure_format = "%Y-%m-%d %H:%M"

    def __init__(self, flight_num, departure):
        self.flight_num = flight_num
        self.departure = departure
        self.passengers = list()


    @property
    def departure(self):
        return self.__departure

    @departure.setter
    def departure(self, value):
        if isinstance(value, datetime) and value > datetime.now():
            self.__departure = value
            return
        if isinstance(value, str):
            value = datetime.strptime(value, self.departure_format)
            if value and value > datetime.now():
                self.__departure = value
                return
        print(f"Error! Incorrect value for the departure date and time")
        self.__departure = None


    def add_passenger(self, p):
        if type(p) is not Passenger:
            print(f"Error! Wrong input: expected a Passenger object, got {type(p)} object")
            return
        if (p not in self.passengers) and p.is_COVID_safe:
            self.passengers.append(p)
            print(f"Successfully added: {p}")
        else:
            print(f"Error, passenger {p.name} could not be added, since the passenger "
                  f"{'is already in the passengers list' if p in self.passengers else 'does not have a valid COVID permit'}")

    def __str__(self):
        flight_str = f"Data about flight number {self.flight_num}:\n"
        flight_str += f"Scheduled for departure at {datetime.strftime(self.departure, self.departure_format)}.\n" \
            if self.departure else "Departure date and time still unknown.\n"
        if len(self.passengers) == 0:
            flight_str += "Still no registered passengers."
        else:
            flight_str += "Passengers:\n" + "\n".join([str(p) for p in self.passengers])
        return flight_str


    def time_till_departure(self):
        pass


    def __iter__(self):
        pass

    def __next__(self):
        pass


if __name__ == '__main__':

    lh1411 = Flight('LF1411', '2022-12-05 6:50')
    lh992 = Flight('LH992', '2022-11-25 12:20')

    print("\nFLIGHTS DATA:\n")
    print(lh1411)
    print()
    print(lh992)

    print()

    bob = Passenger("Bob Smith", "Serbia", "123456", True)
    john = Passenger("John Smith", "Spain", 987656, True)
    jane = Passenger("Jane Smith", "Italy", "987659")
    mike = Passenger.covid_free_Aussie_passenger("Mike Brown", "123654")

    for p in [bob, john, jane, mike]:
        lh1411.add_passenger(p)

    print("\nTRYING TO ADD A PASSENGER WHO IS ALREADY IN THE PASSENGERS LIST")
    lh1411.add_passenger(Passenger("J Smith", "Spain", "987656", True))
    print()

    print(f"\nFLIGHTS DATA AFTER ADDING PASSENGERS TO THE FLIGHT {lh1411.flight_num}:\n")
    print(lh1411)

    print()

    days, hours, mins = lh1411.time_till_departure()
    print(f"Time till departure of the flight {lh1411.flight_num}: {days} days, {hours} hours, and {mins} minutes")

    print()
    print("\nPASSENGERS ON FLIGHT LH1411 (iter / next):")
    flight_iter = iter(lh1411)

    try:
        while True:
            print(next(flight_iter))
    except StopIteration:
        print("No more passengers")

    print()

    print("\nPASSENGERS ON FLIGHT LH1411 (FOR loop):")
    for passenger in lh1411:
        print(passenger)



