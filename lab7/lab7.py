#%%
"""
LAB 7
"""

import io_util as util
from sys import stderr
from datetime import time
import csv
import json
from collections import namedtuple


#%%
"""
TASK 1:

Write the *read_sort_write* function that reads in the content of the given text file,  
sorts it, and writes the (sorted) content to new textual files.
Assume that the content of the given file consists of file names, some of which 
have an extension ('hello.txt'), others do not ('results').
Each file name is given in a separate line.
Sorting should be case insensitive and done in the ascending alphabetical order, as follows:
- for files with extension: first based on the extension and then based on the file name,
- for files without extension, based on the file name.
After sorting, file names with extension should be writen in one textual file 
(e.g., "task1_files_with_extension.txt") and file names without extension in another text 
file (e.g. "task1_files_no_extension.txt")
Include appropriate try except blocks to prevent program from crushing in case of a non 
existing file, or any other problem occurring while reading from / writing to a file.

To test the function, use the 'data/file_names_sample.txt' file
"""
#%%

def read_sort_write(fpath):

    def advanced_file_sort(fname):
        name, ext = fname.rsplit('.', maxsplit=1)
        return ext.lower(), name.lower()

    try:
        with open(fpath, 'r') as fobj:
            lines = [line.strip('\n') for line in fobj.readlines()]
    except FileNotFoundError as err:
        stderr.write(f"{err}\n")
    except OSError as err:
        stderr.write(f"Error when trying to read text from the {fpath.name} file:\n{err}\n")
    else:
        no_ext = []
        with_ext = []
        for line in lines:
            if '.' in line:
                with_ext.append(line)
            else:
                no_ext.append(line)
        no_ext.sort(key=lambda fname: fname.lower())
        with_ext.sort(key=advanced_file_sort)

        util.write_to_txt_file(*with_ext, fpath=util.get_results_dir() / 'task1_files_with_extension.txt')
        util.write_to_txt_file(*no_ext, fpath=util.get_results_dir() / 'task1_files_no_extension.txt')


#%%
# Test the function using the file 'file_names_sample.txt' in the data directory
# read_sort_write(util.get_data_dir() / 'file_names_sample.txt')


#%%
"""
TASK: 2

The file 'cities_and_times.txt' contains city names and time data.
More precisely, each line contains the name of a city, followed by
abbreviated weekday (e.g. "Sun"), and the time in the form "%H:%M".
Write the 'process_city_data' function that reads in the file and 
creates a time-ordered list of the form:
[('San Francisco', 'Sun', datetime.time(0, 52)),
 ('Las Vegas', 'Sun', datetime.time(0, 52)), ...].
Note that the hour and minute data are used to create an object of
the type datetime.time.
The function should also:
- serialise (pickle) the list into a file, as a list object
- write the list content into a csv file, in the format:
   city; weekday; time
  where time is represented in the format '%H:%M:%S'
Include appropriate try except blocks to prevent the program from crushing
in the case of a non existing file, or a problem while reading from / writing to 
a file, or transforming data values.

Note: for a list of things that can be pickled, see this page:
https://docs.python.org/3/library/pickle.html#pickle-picklable

Bonus 1: try using named tuple (collections.namedtuple) to represent and
then manipulate the data read from the text file
The following article can help you learn more about named tuples:
https://realpython.com/python-namedtuple/  

Bonus 2: when testing the function, use csv.DictReader
to read in and print the content of the csv file
"""
#%%

CityTime = namedtuple("CityTime", "city day time")

def process_city_data(fpath):

    lines = util.read_from_txt_file(fpath)
    if len(lines) == 0:
        stderr.write(f"Could not read file data from {fpath} --> Cannot proceed!\n")
        return

    cities = []
    for line in lines:
        city, day, time_str = line.rsplit(maxsplit=2)
        hour, min = time_str.split(':')
        try:
            city_time = CityTime(city, day, time(int(hour), int(min)))
            cities.append(city_time)
            # cities.append((city, day, time(int(hour), int(min))))
        except ValueError as err:
            stderr.write(f"Error when parsing time data for {city}: {err}\n")

    # cities.sort(key=lambda city_data: city_data[2])
    cities.sort(key=lambda city_data: city_data.time)

    util.serialise_to_file(cities, util.get_results_dir() / 'cities_and_times.pkl')
    write_cities_to_csv(cities, util.get_results_dir() / 'cities_and_times.csv')


def write_cities_to_csv(cities_data, fpath):
    try:
        with open(fpath, 'w') as fobj:
            csv_writer = csv.writer(fobj, delimiter=';')
            csv_writer.writerow(CityTime._fields)
            # csv_writer.writerow(('city', 'weekday', 'time'))
            for cdata in cities_data:
                # city_name, city_day, city_time = city
                # csv_writer.writerow((city_name, city_day, time.strftime(city_time, '%H:%M:%S')))
                csv_writer.writerow((cdata.city, cdata.day, time.strftime(cdata.time, "%H:%M:%S")))
    except csv.Error as err:
        stderr.write(f"Error when writing to csv, raised in the 'write_cities_to_csv' function: {err}\n")
    except OSError as err:
        stderr.write(f"Error {type(OSError)} raised in the 'write_cities_to_csv' function: {err}\n")


#%%
# Test the function
# process_city_data(util.get_data_dir() / "cities_and_times.txt")


#%%
# Restore and print the serialised data
# cities = util.unpickle_from_file(util.get_results_dir() / 'cities_and_times.pkl')
# for city in cities:
#     print(city)

#%%
# Restore and print data from the csv file, using csv.DictReader
# try:
#     with open(util.get_results_dir() / 'cities_and_times.csv') as fobj:
#         cities_dict_list = csv.DictReader(fobj, delimiter=';')
#         for city_dict in cities_dict_list:
#             city, wday, time_str = city_dict.values()
#             print(f"{city}, {wday}, {time_str}")
#
# except csv.Error as err:
#     stderr.write(f"Error when reading cities data from csv: {err}\n")


#%%
"""
TASK 3:

In the data folder, there is a text file ('image_files_for_training.txt') that lists 
file paths for a bunch of images (one image file path per line). 
Write the 'process_image_files' function that reads in the content of this text file 
and does the following:
- counts the number of images in each category, and stores the computed
  counts in a csv file ('task3_img_category_stats.csv') in the format: category, image_count
- creates and stores (in a file) a dictionary with the image category as  
  the key and a list of image names in the corresponding category as value;
  for storage use 
  1) pickle ('task3_image_category_data.pkl'), and 
  2) json ('task3_image_category_data.json').
"""

#%%

def process_image_files(fpath):
    from collections import defaultdict

    def write_to_csv(fcsv):
        try:
            with open(fcsv, 'w') as fobj:
                csv_dict_writer = csv.DictWriter(fobj, ['Category', 'ImageCount'])
                csv_dict_writer.writeheader()
                for cat, img_list in img_dict.items():
                    csv_dict_writer.writerow({'Category':cat, 'ImageCount': len(img_list)})
        except csv.Error as err:
            stderr.write(f"Error when writing to csv file {fcsv}:\n{err}\n")

    lines = util.read_from_txt_file(fpath)
    if len(lines) == 0:
        stderr.write(f"Could not read file data from {fpath} --> Cannot proceed!\n")
        return

    img_dict = defaultdict(list)
    for line in lines:
        img_fpath, img_fname = line.rsplit('/', maxsplit=1)
        _, img_dir = img_fpath.lstrip('/').split('/', maxsplit=1)
        img_dict[img_dir].append(img_fname)

    write_to_csv(util.get_results_dir() / 'task3_img_category_stats.csv')

    util.serialise_to_file(img_dict, util.get_results_dir() / 'task3_image_category_data.pkl')

    util.write_to_json(img_dict, util.get_results_dir() / 'task3_image_category_data.json')


#%%
# Test the function
# process_image_files(util.get_data_dir() / "image_files_for_training.txt")


#%%
# Read in and print data stored in the csv file
# try:
#     with open(util.get_results_dir() / 'task3_img_category_stats.csv', 'r') as fobj:
#         img_category_stats_list = csv.DictReader(fobj)
#         for img_cat_stats in img_category_stats_list:
#             cat, img_cnt = img_cat_stats.values()
#             print(f"\t-{cat}: {img_cnt}")
# except csv.Error as err:
#     stderr.write(f"Error when reading image category stats from csv: {err}\n")

#%%
# Read in and print data stored in the json file
# img_cat_dict = util.read_from_json(util.get_results_dir() / 'task3_image_category_data.json')
# for img_cat, img_list in img_cat_dict.items():
#     print(f"{img_cat.upper()}: {','.join(img_list)}")


#%%
"""
Write the 'identify_shared_numbers' function that receives two text files 
with lists of numbers (integers), one number per line. 
The function identifies the numbers present in both lists and stores them
in a new list. 
Finally, the function creates the results dictionary and serialises it to 
a json file ('task4_results.json'). The results dictionary should have the 
following structure:
{
    name_of_the_1st_file: list_of_numbers_from_the_1st_file,
    name_of_the_2nd_file: list_of_numbers_from_the_2nd_file,
    'common_numbers': list_of_the_identified_common_numbers
}

Note: it may happen that not all lines in the input files contain numbers, so,
ensure that only numerical values are considered for comparison.

To test the function use the files 'happy_numbers.txt' and 'prime_numbers.txt'
available in the 'data' folder.

Note: inspired by this exercise:
https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
"""
#%%

def identify_shared_numbers(fpath1, fpath2):

    def to_numbers(str_lines):
        numbers = []
        for ind, line in enumerate(str_lines):
            try:
                numbers.append(int(line))
            except ValueError as err:
                stderr.write(f"Error in transforming str to int, line {ind+1}: {err}\n")
        return numbers

    f1_lines = util.read_from_txt_file(fpath1)
    f2_lines = util.read_from_txt_file(fpath2)

    if len(f1_lines) == 0 or len(f2_lines) == 0:
        stderr.write("Cannot proceed: at list one of the files is empty")
        return

    f1_numbers = to_numbers(f1_lines)
    f2_numbers = to_numbers(f2_lines)
    common_numbers = [num for num in f1_numbers if num in f2_numbers]

    result_dict = dict()
    result_dict[fpath1.name] = f1_numbers
    result_dict[fpath2.name] = f2_numbers
    result_dict['common_numbers'] = common_numbers

    util.write_to_json(result_dict, util.get_results_dir() / 'task4_results.json')



#%%
# Test the function
# t4_f1 = util.get_data_dir() / "prime_numbers.txt"
# t4_f2 = util.get_data_dir() / "happy_numbers.txt"
# identify_shared_numbers(t4_f1, t4_f2)


#%%
# Read in and print data stored in the json file
# res_dict = util.read_from_json(util.get_results_dir() / 'task4_results.json')
# for item, numbers in res_dict.items():
#     print(f"{item}: {','.join([str(num) for num in numbers])}")



#%%
"""
TASK 5:
Write a function (collect_and_store_team_data) that prompts the user for name, age, and competition score 
(0-100) of members of a sports team. 
All data items for one member should be entered in a single line, separated by a comma (e.g. Bob, 19, 55). 
The entry stops when the user enters 'done'.
The function stores the data for each team member as a dictionary, such as
{name:Bob, age:19, score:55.5}
where name is string, age is integer, and score is a real value.
The data for all team members should form a list of dictionaries.
The function prints this list sorted by the members' scores (from highest to lowest) and
then serialise the list to i) a .json file and ii) a .pkl file. 
"""

#%%

def collect_and_store_team_data():
    team_members = []

    print("""
        Please enter team member data in the following way:
        name, age, competition score (0-100)
        Enter 'done' to terminate the process
    """)
    while True:
        data_str = input("Please enter the data for the next team member:\n")
        if data_str.lower() == 'done':
            break
        parts = data_str.split(',')
        if len(parts) == 3:
            name, age, score = parts
            try:
                team_members.append({'name': name, 'age': int(age), 'score': float(score)})
            except ValueError as err:
                print("Incorrect input, please check the guidelines for data entry and try again")
                continue
        else:
            print("Incorrect input, please check the guidelines for data entry and try again")

    for member in sorted(team_members, key=lambda m: m['score'], reverse=True):
        name, age, score = member.values()
        print(f"\t-{name}, age {age}, scored {score}")

    util.write_to_json(team_members, util.get_results_dir() / 'task5_team_members_data.json')
    util.serialise_to_file(team_members, util.get_results_dir() / 'task5_team_members_data.pkl')




#%%

# collect_and_store_team_data()


#%%
"""
TASK 6

Write the 'flights_to_json' function that receives i) an arbitrary number of objects of the
Flight class and ii) name of the json file where the objects should be serialised to. 
The Flight class is defined in the flight module, of the lab6 package.  

Write another function - flights_from_json - that reads, from a json file (given as the input argument), 
data about flights and reconstructs objects of the aforementioned Flight class. The function prints the flights,
in the chronological order of their departure date and time. 

Hint: use the pyjson_trick package
Check the docs for json-tricks at: https://json-tricks.readthedocs.io/en/latest/

"""
#%%
import json_tricks

def flights_to_json(*flights, fpath):
    try:
        with open(fpath, 'w') as fobj:
            json_tricks.dump(flights, fobj, indent=4)
    except Exception as e:
        stderr.write(f"An exception of type {type(e)} raised when writing flights data to file {fpath}\n:{e}\n")


def flights_from_json(fpath):
    try:
        with open(fpath, 'r') as fobj:
            flights = json_tricks.load(fobj)
            for flight in sorted(flights, key=lambda fl: fl.departure):
                print(flight)
                print()

    except Exception as e:
        stderr.write(f"An exception of type {type(e)} raised when reading an object sequence from file {fpath}\n:{e}\n")

#%%
# Create a few flight objects to test the functions

# from lab6.flight import Flight
#
# lh1411 = Flight('LH1411', '2023-03-20 6:50', ('Belgrade', 'Munich'))
#
# lh992 = Flight('LH992', '2023-02-25 12:20', 'Belgrade > Frankfurt', 'Lufthansa')
#
# lh1514_dict = {'fl_num':'lh1514',
#                'departure': '2022-12-30 16:30',
#                'operator': 'Lufthansa',
#                'origin': 'Paris',
#                'destination': 'Berlin'}
# lh1514 = Flight.from_dict(lh1514_dict)
#
# flights = [lh1411, lh992, lh1514]

#%%
# Serialise flight objects to a json file and read them back
# flights_to_json(*flights, fpath=util.get_results_dir() / "sample_flights.json")
#
# flights_from_json(util.get_results_dir() / "sample_flights.json")


#%%
# Add a few passengers to one of the flights and check again the serialisation/ deserialisation

# from lab6.passenger import EconomyPassenger, BusinessPassenger, FlightService
#
# jim = EconomyPassenger("Jim Jonas", 'UK', '123456')
# bill = EconomyPassenger("Billy Stone", 'USA', "917253", is_covid_safe=True)
# dona = EconomyPassenger("Dona Stone", 'Australia', "917251", is_covid_safe=True)
# kate = BusinessPassenger(name="Kate Fox",
#                          country='Canada',
#                          passport="114252",
#                          is_covid_safe=True,
#                          services=[FlightService.ONBOARD_WIFI, FlightService.MEAL])
# bob = BusinessPassenger(name="Bob Smith", country='UK', passport="123456", checked_in=True)
#
# passengers = [jim, bill, dona, kate, bob]
# airfares = [450, 950, 1500, 1000, 475]
# for p, fare in zip(passengers, airfares):
#     lh992.add_passenger(p, fare)

# flights_to_json(*flights, fpath=util.get_results_dir() / "sample_flights.json")
# flights_from_json(util.get_results_dir() / "sample_flights.json")
