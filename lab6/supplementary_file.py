"""
Auxiliary file for Lab 6
"""

"""
__str__ for the Passenger class
"""


# def __str__(self):
#     passenger_str = f"{self.name}\n\tcountry: {self.country}\n\tpassport number: " \
#                     f"{self.passport if self.passport else 'unknown'}\n"
#     passenger_str += f"\tCOVID status: {'valid' if self.is_COVID_safe else 'invalid'}\n"
#     passenger_str += f"\tchecked in: {'yes' if self.checked_in else 'not yet'}\n"
#     passenger_str += f"\tairfare: {self.airfare if self.airfare else 'not paid yet'}\n"
#     passenger_str += f"\textra services: {self.get_services_as_str()}"
#     return passenger_str


"""
# __str__ for the Flight class
"""

# def __str__(self):
#     flight_str = f"Data about flight {self.flight_num}:\n"
#     flight_str += f"Departure date and time: " \
#                   f"{datetime.strftime(self.departure, self.departure_format) if self.departure else 'unknown'}\n"
#
#     if self.route:
#         origin, dest = self.route
#         flight_str += f"Route: {origin} -> {dest}\n"
#     if self.operated_by:
#         flight_str += f"Flight operator: {self.operated_by}\n"
#     if len(self.passengers) == 0:
#         flight_str += "Passengers: none yet"
#     else:
#         flight_str += "Passengers:\n\t" + "\n\t".join([str(p) for p in self.passengers])
#     return flight_str

