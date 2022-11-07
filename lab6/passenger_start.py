#%%
"""
LAB 6, class Passenger
"""

from datetime import datetime, timedelta
from flight_enums import FlightService, COVIDEvidenceType


#%%
"""
Modify the Passenger class from Lab5 as follows:

In addition to the existing attributes, the class should also have the following attributes:
- airfare - the price the passenger has paid for the flight
- checked_in - a boolean indicator, true if the passenger has checked in 
- services - the attribute represents a list of flight services available to the passenger; 
  these services are expected to be instances of the FlightService enumeration.

The following methods of the Passenger class need to be revised:

- constructor (__init__()) - it receives 6 input arguments, one for each attribute except the 
  *services* attributes. The arguments for the passenger's name, country, and passport 
  have to be specified; the arguments for *checked_in* and *is_COVID_safe* are False by default;
  the argument for *airfare* is None by default. The *services* attribute should be initialised 
  to an empty list.

- a method that returns a string representation of a given Passenger object (__str__()) so that it describes 
  the passenger with the extended set of attributes.

Finally, the following new methods should be added:

- get and set methods (using appropriate decorators) for the *airfare* attribute; the attribute 
  should be made private; the set method: 
  i) should assure that a positive numeric value is assigned to this attribute, and 
  ii) should be able to handle both float and string value as the input argument

- get and set methods (using appropriate decorators) for the *checked_in* attribute; the attribute 
  should be made private; the set method should assure that a passenger can check in only if they 
  are COVID safe and have paid the airfare (*airfare* attribute is not None)
"""

#%%
class Passenger:

    def __init__(self, name, country, passport, is_covid_safe=False):
        self.name = name
        self.country = country
        self.passport = passport
        self.is_COVID_safe = is_covid_safe

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, value):
        if isinstance(value, str) and len(value) == 6 and all([ch.isdigit() for ch in value]):
            self.__passport = value
            return
        if isinstance(value, int) and len(str(value)) == 6:
            self.__passport = str(value)
            return
        print(f"Invalid passport number ({value})")
        self.__passport = None


    def __str__(self):
        passenger_str = f"Passenger {self.name} from {self.country} and passport number " \
                        f"{self.passport if self.passport else 'unknown'}"
        passenger_str += f"; {'has' if self.is_COVID_safe else 'does NOT have'} valid COVID permit"
        return passenger_str


    def update_COVID_safe(self, evidence_type, evidence_date):
        if not COVIDEvidenceType.is_valid_evidence_type(evidence_type):
            print(f"Invalid evidence type ({evidence_type}). Cannot proceed!")
            return
        evidence_date = self.get_date(evidence_date)
        if not evidence_date:
            print(f"Invalid evidence date ({evidence_date}). Cannot proceed!")
            return
        if COVIDEvidenceType.is_vaccinated(evidence_type):
            self.is_COVID_safe = evidence_date + timedelta(days=365) > datetime.now()
        elif COVIDEvidenceType.is_tested_negative(evidence_type):
            self.is_COVID_safe = evidence_date + timedelta(days=3) > datetime.now()

    @staticmethod
    def get_date(date_val):
        if isinstance(date_val, datetime):
            return date_val
        elif isinstance(date_val, str):
            return datetime.strptime(date_val, "%d/%m/%Y")
        return None

    @classmethod
    def covid_free_Aussie_passenger(cls, name, passport):
        return cls(name, 'Australia', passport, True)

    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        if self.passport and other.passport and self.country and other.country:
            return other.passport == self.passport and other.country == self.country
        else:
            print(f"Required data is missing for at least one passenger -> Cannot verify identity")
            return False


#%%
"""
Create the EconomyPassenger class that extends the Passenger class and has:

- method add_service_selection that receives a dictionary where keys are services the passenger has bought
  while values are the prices paid for those services. The services should be added to the passenger's 
  *services* list, while the prices should be used to increase the value of the *airfare* attribute, 
  BUT only if the main airfare has been paid.
  The method should also print a report about the added services and the resulting increase in the airfare. 
  Note: keys in the input dictionary are expected to be instances of the FlightService enumeration.  

- overridden __str__ method so that it first prints "Economy class passenger" and then the available information 
  about the passenger
"""

#%%




#%%
"""
Create class BusinessPassenger that extends the Passenger class and has:

- the constructor (__init__()) that receives the same arguments as the constructor of the upper class
  plus services to be assigned to the *services* attribute. This additional argument should be a tuple 
  of either strings (service names) or elements of the FlightService enumeration; its default value
  is FlightService.UNSPECIFIED. The method should check the validity of the tuple elements before adding 
  them to the *services* attribute. 
  Important: the constructor should be written in a way that makes the class ready for multiple inheritance.

- overridden __str__ method so that it first prints "Business class passenger" and then 
  the available information about the passengers

"""


#%%




#%%

if __name__ == '__main__':
    pass

    # jim = EconomyPassenger("Jim Jonas", 'UK', '123456', airfare=450, is_covid_safe=True)
    # print(jim)
    # print()
    #
    # # Add extra services to Jim
    # extra_services = {
    #     FlightService.REFRESHMENTS: 10,
    #     FlightService.ONBOARD_MEDIA: 15
    # }
    # jim.add_service_selection(extra_services)
    #
    # bob = EconomyPassenger("Bob Jones", 'Denmark', '987654')
    # print(bob)
    # print()
    #
    # mike = BusinessPassenger(name="Mike Stone", country="USA",
    #                          passport='234567', is_covid_safe=True,
    #                          services=(FlightService.PRIORITY_BOARDING, FlightService.ONBOARD_WIFI))
    # print(mike)
    # print()
    # print(mike.__dict__)
    #
    # brian = BusinessPassenger(name="Brian Brown", country="UK",
    #                           passport='546234', is_covid_safe=True,
    #                           services=("priority boarding", "onboard media", "drinks"))
    # print(brian)
