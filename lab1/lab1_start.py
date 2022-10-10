#%%
# Task 1
# Write a function that asks the user for a number, and depending on whether
# the number is even or odd, prints out an appropriate message.



#%%
# Test the function
# odd_or_even()


#%%
# Task 2
# Write a function to calculate the factorial of a number.
# The function accepts the number (a positive integer)
# as an argument. The computed factorial value should be
# printed to the console.



#%%
# Test the function
# factorial(5)


#%%
# Task 3
# Write a function that returns the lowest n-th value of an iterable
# (1st input parameter). The function returns the lowest
# value if n (2nd input parameter) is non-positive or greater
# than the number of elements in the iterable.




#%%
# Test the function with...
# ... a sequence of numbers:
# a = [31, 72, 13, 41, 5, 16, 87, 98, 9]
# print("3rd lowest in [31, 72, 13, 41, 5, 16, 87, 98, 9]:")
# print(nth_lowest(a, 3))

# ... a sequence of letters:
# print("6th lowest in ['f', 'r', 't', 'a', 'b', 'y', 'j', 'd', 'c']:")
# print(nth_lowest(['f', 'r', 't', 'a', 'b', 'y', 'j', 'd', 'c'], 6))

# ... a string:
# print("2nd lowest in 'today':")
# print(nth_lowest('today', 2))


#%%
# Task 4
# Write a function that receives a list of numbers and returns
# a tuple with the following elements:
# - the list element with the smallest absolute value
# - the list element with the largest absolute value
# - the sum of all non-negative elements in the list
# - the product of all negative elements in the list




#%%
# Test the function
# print(list_stats([3.4, 5.6, -4.2, -5.6, 9, 1.2, 11.3, -23.45, 81]))


#%%
# Task 5
# Write a function that receives a list of numbers and a
# threshold value (number). The function:
# - makes a new list that has unique elements from the input list
#   that are below the threshold
# - prints the number of elements in the new list
# - sorts the elements in the new list in the descending order,
#   and prints them, one element per line




#%%
# Test the function
# list_operations([1, 1, 2, 3, 5, 8, 13, 5, 21, 34, 55, 89], 20)


#%%
# Task 6
# Write a function that receives two strings and checks if they
# are anagrams. The function returns appropriate boolean value.
# Note: An anagram is a word or phrase formed by rearranging the
# letters of a different word or phrase, typically using all the
# original letters exactly once




#%%
# Test the function
# print("anagrams('School master', 'The classroom'):")
# print(anagrams('School master', 'The classroom'))
# print("anagrams('Dormitory', 'Dirty room'):")
# print(anagrams('Dormitory', 'Dirty room'))
# print("anagrams('Conversation', 'Voices rant on'):")
# print(anagrams('Conversation', 'Voices rant on'))
# print("anagrams('Bob', 'Bill'):")
# print(anagrams('Bob', 'Bill'))


#%%
# Task 7
# Write a function that receives a string and checks if the
# string is palindrome. The function returns appropriate boolean value.
# Note: a palindrome is a word, phrase, or sequence that reads the same
# backwards as forwards, e.g. "madam" or "nurses run".




#%%
# Test the function
# print("palindrome('Madam'):")
# print(palindrome("Madam"))
# print("palindrome('nurses run'):")
# print(palindrome("nurses run"))
# print("palindrome('nurse run'):")
# print(palindrome("nurse run"))


#%%
# Task 8
# Write a function to play a guessing game: to guess a number between 1 and 9.
# Scenario: user is prompted to enter a guess. If the user guesses wrongly,
# the prompt reappears; the user can try to guess max 3 times;
# on successful guess, user should get a "Well guessed!" message,
# and the function terminates. If when guessing, the user enters a number
# that is out of the bounds (less than 1 or greater than 9), or a character
# that is not a number, they should be informed that only single digit
# values are allowed.
#
# Hint: use function randint from random package to generate a number to
# be guessed in the game





#%%
# Test the function
# guessing_game()


#%%
if __name__ == '__main__':
    pass

    # odd_or_even()
    #
    # factorial(7)
    #
    # a = [31, 72, 13, 41, 5, 16, 87, 98, 9]
    # print("3rd lowest in [31, 72, 13, 41, 5, 16, 87, 98, 9]:")
    # print(nth_lowest(a, 3))
    # print("6th lowest in ['f', 'r', 't', 'a', 'b', 'y', 'j', 'd', 'c']:")
    # print(nth_lowest(['f', 'r', 't', 'a', 'b', 'y', 'j', 'd', 'c'], 6))
    # print("2nd lowest in 'today':")
    # print(nth_lowest('today', 2))
    #
    # print(list_stats([3.4, 5.6, -4.2, -5.6, 9, 1.2, 11.3, -23.45, 81]))
    #
    # list_operations([1, 1, 2, 3, 5, 8, 13, 5, 21, 34, 55, 89], 20)
    #
    # print("anagrams('School master', 'The classroom'):")
    # print(anagrams('School master', 'The classroom'))
    # print("anagrams('Dormitory', 'Dirty room'):")
    # print(anagrams('Dormitory', 'Dirty room'))
    # print("anagrams('Conversation', 'Voices rant on'):")
    # print(anagrams('Conversation', 'Voices rant on'))
    # print("anagrams('Bob', 'Bill'):")
    # print(anagrams('Bob', 'Bill'))
    #
    # print("palindrome('madam'):")
    # print(palindrome("madam"))
    # print("palindrome('nurses run'):")
    # print(palindrome("nurses run"))
    # print("palindrome('nurse run'):")
    # print(palindrome("nurse run"))
    #
    # guessing_game()