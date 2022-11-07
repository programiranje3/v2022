"""
LAB 6, enums
"""

from enum import Enum

"""
The FlightService enumeration defines various kinds of services that can be offered to passengers, 
plus an item for cases when services are not specified.
"""

class FlightService(Enum):
    SNACK = 'snack'
    REFRESHMENTS = 'refreshments'
    MEAL = 'meal'
    PRIORITY_BOARDING = 'priority boarding'
    ONBOARD_WIFI = 'onboard wifi'
    ONBOARD_MEDIA = 'onboard media'
    UNSPECIFIED = 'unspecified'

    @staticmethod
    def valid_service_str(str_value):
        return any([str_value in [s.value, s.name] for s in FlightService])

    @staticmethod
    def get_service_from_str(str_value):
        if FlightService.valid_service_str(str_value):
            for s in FlightService:
                if str_value in [s.name, s.value]:
                    return s
        return None


"""
The COVIDEvidenceType enumeration from Lab 5
"""
class COVIDEvidenceType(Enum):
    VACCINATED = "vaccinated"
    TESTED_NEGATIVE = "tested negative"

    @staticmethod
    def is_valid_evidence_type(value):
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
