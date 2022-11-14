#%%
"""
LAB 7
"""



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
('task1_files_with_extension.txt') and file names without extension in another text 
file ('task1_files_no_extension.txt')
Include appropriate try except blocks to prevent program from crushing in case of a non 
existing file, or any other problem occurring while reading from / writing to a file.

To test the function, use the 'data/file_names_sample.txt' file
"""
#%%



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
- serialise (pickle) the list into a file ('task2_cities_and_times.pkl'), as a list object
- write the list content into a csv file ('task2_cities_and_times.csv'), in the format:
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



#%%
# Test the function
# process_city_data(util.get_data_dir() / "cities_and_times.txt")


#%%
# Restore and print the serialised data


#%%
# Restore and print data from the csv file


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



#%%
# Test the function
# process_image_files(util.get_data_dir() / "image_files_for_training.txt")


#%%
# Read in and print data stored in the csv file


#%%
# Read in and print data stored in the json file



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




#%%
# Test the function
# t4_f1 = util.get_data_dir() / "prime_numbers.txt"
# t4_f2 = util.get_data_dir() / "happy_numbers.txt"
# identify_shared_numbers(t4_f1, t4_f2)


#%%
# Read in and print data stored in the json file



#%%
"""
TASK 5:
Write a function that prompts the user for name, age, and competition score (0-100) of members of a sports team. 
All data items for one member should be entered in a single line, separated by a comma (e.g. Bob, 19, 55). 
The entry stops when the user enters 'done'.
The function stores the data for each team member as a dictionary, such as
{name:Bob, age:19, score:55}
where name is string, age is integer, and score is a real value.
The data for all team members should form a list of dictionaries.
The function prints this list sorted by the members' scores (from highest to lowest) and
then serialise the list to i) a .json file and ii) a .pkl file. 
"""

#%%


#%%
# collect__and_store_team_data()


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



#%%
# Create a few flight objects to test the functions

# from lab6.flight import Flight
#
# lh1411 = Flight('LH1411', '2023-03-20 6:50', ('Belgrade', 'Munich'))
#
# lh992 = Flight('LH992', '2023-02-25 12:20', 'Belgrade -> Frankfurt', 'Lufthansa')
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

# Serialise flight objects to a json file and read them back
