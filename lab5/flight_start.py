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


if __name__ == '__main__':

    pass

    # lh1411 = Flight('LF1411', '2022-12-05 6:50')
    # lh992 = Flight('LH992', '2022-11-25 12:20')
    #
    # print("\nFLIGHTS DATA:\n")
    # print(lh1411)
    # print()
    # print(lh992)
    #
    # print()
    #
    # bob = Passenger("Bob Smith", "Serbia", "123456", True)
    # john = Passenger("John Smith", "Spain", 987656, True)
    # jane = Passenger("Jane Smith", "Italy", "987659")
    # mike = Passenger.covid_free_Aussie_passenger("Mike Brown", "123654")
    #
    # for p in [bob, john, jane, mike]:
    #     lh1411.add_passenger(p)
    #
    # print("\nTRYING TO ADD A PASSENGER WHO IS ALREADY IN THE PASSENGERS LIST")
    # lh1411.add_passenger(Passenger("J Smith", "Spain", "987656", True))
    # print()
    #
    # print(f"\nFLIGHTS DATA AFTER ADDING PASSENGERS TO THE FLIGHT {lh1411.flight_num}:\n")
    # print(lh1411)
    #
    # print()
    #
    # days, hours, mins = lh1411.time_till_departure()
    # print(f"Time till departure of the flight {lh1411.flight_num}: {days} days, {hours} hours, and {mins} minutes")
    #
    # print()
    # print("\nPASSENGERS ON FLIGHT LH1411 (iter / next):")
    #
    #
    # print()
    # print("\nPASSENGERS ON FLIGHT LH1411 (FOR loop):")



