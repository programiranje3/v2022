#%%
"""
LAB 6, class Flight
"""

"""
Modify the Flight class from Lab5 as follows:

In addition to the flight_num, departure, and passengers attributes, the class should also have 
the following attributes:
- route - the route of the flight as a tuple of the form (origin, destination)
- operated_by - the company that operates the flight

The following methods of the Flight class need to be revised:

- the constructor (__init__()) - it should receive 4 input arguments for the *flight_num*, *departure*,
  *route*, and *operated_by* attributes; the arguments for the *route* and *operated_by* attributes have default 
  value None; the *passengers* attribute is initialised to an empty list

- the set method for the *departure* attribute, so that it properly handles situations when departure date 
  and time are given as a string in an unknown format (that is, in the format other than the *departure_format*)

- the add_passenger() method for adding a passenger to the flight; in addition to receiving the passenger to 
  be added, the method also receives an argument for the airfare to be paid by the passenger. The method adds 
  the new passenger to the *passengers* list if they are not already in the list. If successfully added, the 
  value of the 2nd argument is assigned to the passenger's airfare attribute.  
  Note: checking for valid COVID permit is now moved to check-in. 

- the method that returns a string representation of the given Flight object (__str__()) so that it describes 
  the flight with the extended set of attributes

Furthermore, the following new methods should be added:

- get and set methods (using appropriate decorators) for the *route* attribute; the set method
  should allow for different ways of setting the route, that is, it should be able to handle input 
  value given as a list or a tuple (of two elements) or a string with the origin and destination 
  separated by a comma (Belgrade, Rome), a hyphen (Belgrade - Rome), or a '>' char (Belgrade > Roma)
  (Hint: consider using split method from the re (regular expressions) module)

- class method from_dict() for creating a Flight object (alternative constructor) out of the flight-related 
  data provided as a dictionary (the only input argument) with the following keys: 
  fl_num, departure, origin, destination, operator. 
  Consider that the dictionary might not contain all the expected items, that is, some dictionary keys might 
  not match the expected ones; in such a case, the method prints the keys that were expected but not available 
  in the input dictionary and returns None 
  
- a generator method that generates a sequence of passengers who have not yet checked in; at the end - after 
  yielding all those who haven't checked in yet - the method prints the number of such passengers.

- a generator method that generates a sequence of candidate passengers for an upgrade to the business class; 
  those are the passengers of the economy class whose airfare exceed the given threshold (input parameter) 
  and who have checked in for the flight; the generated sequence should consider the passengers airfare, 
  so that those who paid more are prioritised for the upgrade option.

"""

#%%

from datetime import datetime
from lab6.passenger import Passenger, EconomyPassenger, BusinessPassenger
from sys import stderr


class Flight:

    departure_format = "%Y-%m-%d %H:%M"

    def __init__(self, flight_num, departure, route=None, operated_by=None):
        self.flight_num = flight_num
        self.departure = departure
        self.route = route
        self.operated_by = operated_by
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
            try:
                value_dt = datetime.strptime(value, self.departure_format)
                if value_dt > datetime.now():
                    self.__departure = value_dt
                    return
            except ValueError as err:
                stderr.write(f"The input string is not in the required datetime format {Flight.departure_format}\n")
                stderr.write(f"Original error: {err}\n")

        stderr.write("Error! Incorrect value for the departure date and time\n")
        self.__departure = None

    @property
    def route(self):
        return self.__route

    @route.setter
    def route(self, value):
        if isinstance(value, (list, tuple)) and len(value) == 2:
            origin, dest = value
            self.__route = origin, dest
            return
        if isinstance(value, str):
            # a comma (Belgrade, Rome), a hyphen (Belgrade - Rome), or a '>' char (Belgrade > Roma)
            import re
            parts = re.split('[,->]', value)
            if len(parts) == 2:
                self.__route = tuple(parts)
                return

        stderr.write(f"Invalid input argument ({value}) for the flight's route\n")
        self.__route = None

    def add_passenger(self, p, airfare):
        if not isinstance(p, Passenger):
            print(f"Error! Wrong input: expected a Passenger object, got {type(p)} object")
            return
        if p not in self.passengers:
            p.airfare = airfare
            self.passengers.append(p)
            print(f"Successfully added:\n{p}")
        else:
            stderr.write(f"Error! Passenger {p.name} is already in the passengers list\n")

    def __str__(self):
        flight_str = f"Data about flight {self.flight_num}:\n"
        flight_str += f"Departure date and time: " \
                      f"{datetime.strftime(self.departure, self.departure_format) if self.departure else 'unknown'}\n"
        if self.route:
            origin, dest = self.route
            flight_str += f"Route: {origin} -> {dest}\n"
        if self.operated_by:
            flight_str += f"Flight operator: {self.operated_by}\n"
        if len(self.passengers) == 0:
            flight_str += "Passengers: none yet"
        else:
            flight_str += "Passengers:\n\t" + "\n\t".join([str(p) for p in self.passengers])
        return flight_str

    def time_till_departure(self):
        if self.departure:
            time_left = self.departure - datetime.now()
            hours_left, rest_sec = divmod(time_left.seconds, 3600)
            mins_left, _ = divmod(rest_sec, 60)
            return time_left.days, hours_left, mins_left

        print("Departure time is still unknown")
        return None

    def __iter__(self):
        self.__iter_counter = 0
        return self

    def __next__(self):
        if self.__iter_counter == len(self.passengers):
            raise StopIteration
        next_passenger = self.passengers[self.__iter_counter]
        self.__iter_counter += 1
        return next_passenger

    @classmethod
    def from_dict(cls, data_dict):
        try:
            return cls(data_dict['fl_num'],
                       data_dict['departure'],
                       (data_dict['origin'], data_dict['destination']),
                       data_dict['operator'])
        except KeyError as err:
            stderr.write("Error occurred when reading flight-related dictionary data\n")
            keys = {'fl_num', 'departure', 'origin', 'destination', 'operator'}
            missing_keys = keys - set(data_dict.keys())
            stderr.write(f"Data for the following keys are missing: {', '.join(missing_keys)}\n")
            return None


    def not_checkedin_generator(self):
        to_checkin_counter = 0
        for p in self.passengers:
            if not p.checked_in:
                yield p
                to_checkin_counter += 1

        msg = "All passengers have checked in" if to_checkin_counter == 0 else \
            f"Waiting for {to_checkin_counter} passengers to check in"
        print(msg)


    def candidates_for_upgrade_generator(self, min_airfare):
        candidates = []
        for p in self.passengers:
            if isinstance(p, EconomyPassenger) and p.checked_in and p.airfare > min_airfare:
                candidates.append(p)
        for candidate in sorted(candidates, key=lambda c: c.airfare, reverse=True):
            yield candidate

#%%

if __name__ == '__main__':
    pass

    lh1411 = Flight('LH1411', '2023-03-20 6:50', ('Belgrade', 'Munich'))
    print(lh1411)
    print()

    lh992 = Flight('LH992', '2023-02-25 12:20', 'Belgrade > Frankfurt', 'Lufthansa')
    print(lh992)
    print()

    lh1514_dict = {'fl_num': 'lh1514',
                   'departure': '2022-12-30 16:30',
                   'operator': 'Lufthansa',
                   'origin': 'Paris',
                   'destination': 'Berlin'}

    lh1514 = Flight.from_dict(lh1514_dict)
    print(lh1514)
    print()

    jim = EconomyPassenger("Jim Jonas", 'UK', '123456')
    bill = EconomyPassenger("Billy Stone", 'USA', "917253", is_covid_safe=True)
    dona = EconomyPassenger("Dona Stone", 'Australia', "917251", is_covid_safe=True)
    kate = BusinessPassenger(name="Kate Fox", country='Canada', passport="114252", is_covid_safe=True)
    bob = BusinessPassenger(name="Bob Smith", country='UK', passport="123456")

    passengers = [jim, bill, dona, kate, bob]
    airfares = [450, 950, 1500, 1000, 475]
    for p, fare in zip(passengers, airfares):
        lh992.add_passenger(p, fare)

    print(f"\nAfter adding passengers to flight {lh992.flight_num}:\n")
    print(lh992)
    print()

    print("Last call to passengers who have not yet checked in!")
    for passenger in lh992.not_checkedin_generator():
        print(passenger)

    # check in some economy class passengers to be able to test the next method
    dona.checked_in = True
    bill.checked_in = True

    print()
    print("Passengers offered an upgrade opportunity (using for loop)")
    for passenger in lh992.candidates_for_upgrade_generator(500):
        print(passenger)

    print()
    print("Candidates for upgrade to business class (by calling next())")
    g = lh992.candidates_for_upgrade_generator(500)
    try:
        while True:
            print(next(g))
    except StopIteration:
        print("--- end of candidates list ---")