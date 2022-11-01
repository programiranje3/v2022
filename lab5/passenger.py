#%%
"""
LAB 5, class Passenger
"""

"""
Create the Passenger class with the following methods:

- a constructor (__init__()) that receives four input arguments that are used to 
  initialise the following 4 attributes:
     - name - the passenger's name and surname
     - country - the passanger's country of origin
     - passport - the passenger's passport number
     - is_COVID_safe - a boolean indicator variable; it is true if the passenger is vaccinated 
     or has recently been tested negative; the default value of this argument is False

- get and set methods for the *passport* attribute (using appropriate decorators);
  designate this attribute as private and assure that it is a string of length 6,
  consisting of digits only.
  
- a method that returns a string representation of a Passenger object (__str__())

- a method (update_COVID_safe) that sets *is_COVID_safe* based on the value of its input parameters: 
  - evidence type: a string that should be either 'vaccinated' or 'tested negative'
  - evidence date: the date of vaccination / PCR test; if given as a string, it is 
  expected to be in the following format: %d/%m/%Y
  The method sets *is_COVID_safe* to True if:
  - the (last) vaccination was within the last 365 days OR
  - the negative test is not older than 3 days    
  Note: for datetime formatting codes, check this table:
  https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

- class method covid_free_Aussie_passenger for creating a passenger from Australia who is COVID safe
  (alternative constructor); the method receives the passenger's name and passport number.

- a method that checks for equality of the given Passenger object and another object
  that is passed to the method as its input parameter (__eq__()); two passenger objects
  are considered the same if they are citizens of the same country and have the same passport number
"""

#%%

from datetime import datetime, timedelta, date
from enum import Enum

class COVIDEvidenceType(Enum):
    VACCINATED = "vaccinated"
    TESTED_NEGATIVE = "tested negative"

    @staticmethod
    def is_valid_evidence_type(value):
        # Option 1
        # if isinstance(value, COVIDEvidenceType):
        #     return True
        # if isinstance(value, str):
        #     for evidence in COVIDEvidenceType:
        #         if evidence.value == value:
        #             return True
        # return False
        # Option 2
        for evidence in COVIDEvidenceType:
            if evidence == value or evidence.value == value:
                return True
        return False

    @staticmethod
    def is_vaccinated(evidence):
        return COVIDEvidenceType.VACCINATED == evidence or \
               COVIDEvidenceType.VACCINATED.value == evidence

    @staticmethod
    def is_tested_negative(evidence):
        return COVIDEvidenceType.TESTED_NEGATIVE == evidence or \
               COVIDEvidenceType.TESTED_NEGATIVE.value == evidence



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
        if isinstance(date_val, (date, datetime)):
            return date_val
        elif isinstance(date_val, str):
            return datetime.strptime(date_val, "%d/%m/%Y")
        return None

    @classmethod
    def covid_free_Aussie_passenger(cls, name, passport):
        return cls(name, 'Australia', passport, True)

    def __eq__(self, other):
        # Option 1
        # if not isinstance(other, Passenger):
        #     return False
        # Option 2
        if type(self) is not type(other):
            return False
        if self.passport and other.passport and self.country and other.country:
            return other.passport == self.passport and other.country == self.country
        else:
            print(f"Required data is missing for at least one passenger -> Cannot verify identity")
            return False


if __name__ == '__main__':

    bob = Passenger("Bob Smith", "Serbia", "123456", True)
    john = Passenger("John Smith", "Spain", 987656, True)
    jane = Passenger("Jane Smith", "Italy", "987659")
    mike = Passenger.covid_free_Aussie_passenger("Mike Brown", "123654")

    print("PASSENGERS DATA:\n")
    print(bob)
    print(john)
    print(jane)
    print(mike)

    print("\nPASSENGERS DATA AFTER UPDATING COVID STATUS:\n")
    jane.update_COVID_safe('vaccinated', '15/01/2022')
    print(jane)

    mike.update_COVID_safe('tested negative', '25/10/2022')
    print(mike)

    print()
    print("Checking if 'bob' and 'john' refer to the same passenger")
    print(bob == john)


