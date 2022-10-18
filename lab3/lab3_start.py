#%%

"""
LAB 3
"""

#%%
"""
TASK 1:
Write a function that receives an integer value (n) and generates  
a dictionary with entries in the form x: 1 + 2 + ... + x, 
where x is a number between 1 and n.
The function also prints the dictionary in the decreasing value 
of the key, in the following way (for n=5):
5: 1+2+3+4+5=15
4: 1+2+3+4=10
3: 1+2+3=6
2: 1+2=3
1: 1=1
"""




#%%
# Test the function:
# create_print_numeric_dict(7)


#%%
"""
TASK 2:
Write a function that creates a dictionary from the two given lists, so that
elements of the 1st list are keys, while the corresponding elements of the 
2nd list are values. 
Print the dictionary sorted based on the element values.
(hint: use itemgetter() f. from the operator module)

Example: a list of countries and a list of the countries' national dishes
should be turned into a dictionary where keys are country names and values
are the corresponding dishes.
"""



#%%
# Test the function:
# dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
# countries = ["Italy", "Germany", "Spain", "USA", "Serbia"]
# lists_to_dict(countries, dishes)

#%%

"""
TASK 3:
Write a function that receives a string as its input parameter, and
calculates the number of digits, letters, and punctuation marks (.,!?;:)
in this string.
The function returns a dictionary with the computed values.
"""



#%%
# Test the function:
# print("string_stats('Today is November 5, 2021!'):")
# print(string_stats("Today is November 5, 2021!"))


#%%
"""
TASK 4:
Write a function that receives a list of web addresses (= website names) of various organisations.
Compute the number of addresses for each suffix (e.g., com, org, net) encountered in the list.
Create and return a dictionary of thus computed values (keys are website suffixes, values are
the corresponding counts)
"""



#%%
# Test the function:
# sample_websites = ['https://www.technologyreview.com/', 'https://www.tidymodels.org/',
#                    'https://podcasts.google.com/', 'https://www.jamovi.org/', 'http://bg.ac.rs/']
#
# print(website_stats(sample_websites))

#%%
"""
# TASK 5:
Write a function that receives a piece of text and computes the frequency of tokens 
appearing in the text (consider that a token is a string of contiguous characters between two spaces). 
Compute token frequency in case-insensitive manner (do not consider the difference between upper and 
lowercase letters).
Tokens and their frequencies should be stored in a dictionary. 
The function prints tokens and their frequencies after sorting the tokens alphanumerically.

After testing the function, alter it so that:
- tokens are cleared of any excessive characters (e.g. spaces or punctuation marks)
before being added to the dictionary
- only tokens with at least 3 characters are added to the dictionary
- before being printed, the dictionary entries are sorted: 
    i) in the decreasing order of the tokens' frequencies, and then 
    ii) in increasing alphabetical order.
"""




#%%
# Test the function:
#
# response by GPT-3 to the question why it has so entranced the tech community
# source: https://www.wired.com/story/ai-text-generator-gpt-3-learning-language-fitfully/
# gpt3_response = ("""
#         I spoke with a very special person whose name is not relevant at this time,
#         and what they told me was that my framework was perfect. If I remember correctly,
#         they said it was like releasing a tiger into the world.
#     """)
# token_frequency(gpt3_response)

#%%

"""
TASK 6:
Write a function that accepts a sequence of comma separated passwords and
checks their validity using the following criteria:
1. At least 1 letter between [a-z] => At least 1 lower case letter
2. At least 1 number between [0-9] => At least 1 digit
3. At least 1 letter between [A-Z] => At least 1 upper case letter
4. At least 1 of these characters: $,#,@
5. Length in the 6-12 range (including 6 and 12)
The function creates and returns a dictionary with checked passwords as keys, 
whereas the value of a key should be:
- the word "valid" if the corresponding password proved to be valid
- list of identified issues, if the corresponding password is not valid 
"""




#%%
# Test the function:
#
# print("Passwords to check: ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR")
# validation_dict = password_check("ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR")
# print("Validation results:")
# for password, result in validation_dict.items():
#     print(f"- {password}: {', '.join(result)}")

#%%

"""
TASK 7:
Write a function that takes as its input a list of dictionaries with data about members of a sports team.
Each dictionary stores the following data about one team member: name, age, and competition score (0-100).
For example: {name:Bob, age:19, score:55.5} 
The function computes and prints the following statistics:
- the average (mean) age of the team members
- median, first and third quartile for the team's score
- name of the player with the highest score among those under 21 years of age
Finally, the function prints the members list sorted by the members' scores (from highest to lowest).

Hint: the 'statistics' module provides functions for the required computations
"""


#%%
# Test the function:
# team = [{'name': 'Bob', 'age': 18, 'score': 50.0},
#         {'name': 'Tim', 'age': 17, 'score': 84.0},
#         {'name': 'Jim', 'age': 19, 'score': 94.0},
#         {'name': 'Joe', 'age': 19, 'score': 85.5}]
# team_stats(team)

#%%

"""
TASK 8:
Write a function to count the total number of students per class. The function receives
a list of tuples of the form (<class>,<stud_count>). For example:
[('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)]
The function creates a dictionary of classes and their student numbers; it then
prints the classes and their sizes in the decreasing order of the class size.

After testing the function, try writing it using the Counter class from
the collections module.
"""



#%%
# Test the function:
# l = [('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)]
# classroom_stats(l)

#%%
if __name__ == '__main__':
    pass

    # # Task 1
    # create_print_numeric_dict(7)
    # print()
    #
    # # Task 2
    # dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
    # countries = ["Italy", "Germany", "Spain", "USA", "Serbia"]
    # lists_to_dict(countries, dishes)
    # print()
    #
    # # Task 3
    # print("string_stats('Today is November 5, 2021!'):")
    # print(string_stats("Today is November 5, 2021!"))
    # print()
    #
    # # Task 4
    # sample_websites = ['https://www.technologyreview.com/', 'https://www.tidymodels.org/',
    #                    'https://podcasts.google.com/', 'https://www.jamovi.org/', 'http://bg.ac.rs/']
    #
    # print(website_stats(sample_websites))
    # print()
    #
    # # Task 5
    # # response by GPT-3 to the question why it has so entranced the tech community
    # # source: https://www.wired.com/story/ai-text-generator-gpt-3-learning-language-fitfully/
    # gpt3_response = ("""
    #     I spoke with a very special person whose name is not relevant at this time,
    #     and what they told me was that my framework was perfect. If I remember correctly,
    #     they said it was like releasing a tiger into the world.
    # """)
    # token_frequency(gpt3_response)
    # print()
    #
    # # Task 6:
    # print("Passwords to check: ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR")
    # validation_dict = password_check("ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR")
    # print("Validation results:")
    # for password, result in validation_dict.items():
    #     print(f"- {password}: {', '.join(result)}")
    # print()
    #
    # # Task 7:
    # # team = [{'name': 'Bob', 'age': 18, 'score': 50.0},
    # #         {'name': 'Tim', 'age': 17, 'score': 84.0},
    # #         {'name': 'Jim', 'age': 19, 'score': 94.0},
    # #         {'name': 'Joe', 'age': 19, 'score': 85.5}]
    # team_stats(team)
    # print()
    #
    # # Task 8:
    # l = [('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)]
    # classroom_stats(l)