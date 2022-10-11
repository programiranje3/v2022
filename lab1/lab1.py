#%%
# Task 1
# Write a function that asks the user for a number, and depending on whether
# the number is even or odd, prints out an appropriate message.

def odd_or_even():
    num_str = input("Please enter a number\n")
    num = int(num_str)
    # Option 1:
    remainder = num % 2
    # Option 2:
    res, remainder = divmod(num, 2)
    if remainder == 0:
        print(f"Number {num} is EVEN")
    else:
        print(f"Number {num} is ODD")


#%%
# Test the function
odd_or_even()


#%%
# Task 2
# Write a function to calculate the factorial of a number.
# The function accepts the number (a positive integer)
# as an argument. The computed factorial value should be
# printed to the console.

def factorial(number):
    if number <= 0:
        print("Wrong input! Number should be positive.")
    else:
        # f = number * (number-1) * ... * 1
        f = 1
        for x in range(number, 0, -1):
            f *= x
        print(f"Factorial of number {number} is {f}")


#%%
# Test the function
factorial(5)


#%%
# Task 3
# Write a function that returns the lowest n-th value of an iterable
# (1st input parameter). The function returns the lowest
# value if n (2nd input parameter) is non-positive or greater
# than the number of elements in the iterable.

def nth_lowest(iterable, n):
    if n < 0 or n > len(iterable):
        return min(iterable)
    return sorted(iterable)[n-1]

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
print("2nd lowest in 'today':")
print(nth_lowest('today', 2))


#%%
# Task 4
# Write a function that receives a list of numbers and returns
# a tuple with the following elements:
# - the list element with the smallest absolute value
# - the list element with the largest absolute value
# - the sum of all non-negative elements in the list
# - the product of all negative elements in the list

def list_stats(numbers):
    min_abs = max_abs = abs(numbers[0])
    sum_nneg = 0
    prod_neg = 1
    for num in numbers:
        if num >= 0: sum_nneg += num
        else: prod_neg *= num
        if abs(num) > max_abs: max_abs = abs(num)
        elif abs(num) < min_abs: min_abs = abs(num)
    return min_abs, max_abs, sum_nneg, prod_neg



#%%
print(list_stats([3.4, 5.6, -4.2, -5.6, 9, 1.2, 11.3, -23.45, 81]))


#%%
# Task 5
# Write a function that receives a list of numbers and a
# threshold value (number). The function:
# - makes a new list that has unique elements from the input list
#   that are below the threshold
# - prints the number of elements in the new list
# - sorts the elements in the new list in the descending order,
#   and prints them, one element per line

def list_operations(numbers, threshold):
    new_list = list()
    # Option1:
    # for num in numbers:
    #     if (num < threshold) and (num not in new_list):
    #         new_list.append(num)
    # Option 2:
    for num in set(numbers):
        if num < threshold: new_list.append(num)

    print(f"The number of elements in the new list: {len(new_list)}")
    print("New list, sorted in decreasing order:")
    for num in sorted(new_list, reverse=True):
        print(num)


#%%
list_operations([1, 1, 2, 3, 5, 8, 13, 5, 21, 34, 55, 89], 20)


#%%
# Task 6
# Write a function that receives two strings and checks if they
# are anagrams. The function returns appropriate boolean value.
# Note: An anagram is a word or phrase formed by rearranging the
# letters of a different word or phrase, typically using all the
# original letters exactly once

def anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)



#%%
print("anagrams('School master', 'The classroom'):")
print(anagrams('School master', 'The classroom'))
print("anagrams('Dormitory', 'Dirty room'):")
print(anagrams('Dormitory', 'Dirty room'))
print("anagrams('Conversation', 'Voices rant on'):")
print(anagrams('Conversation', 'Voices rant on'))
print("anagrams('Bob', 'Bill'):")
print(anagrams('Bob', 'Bill'))


#%%
# Task 7
# Write a function that receives a string and checks if the
# string is palindrome. The function returns appropriate boolean value.
# Note: a palindrome is a word, phrase, or sequence that reads the same
# backwards as forwards, e.g. "madam" or "nurses run".

def palindrome(string):
    string = string.replace(" ", "").lower()
    #Option 1:
    # str_rev = string[::-1]
    # return string == str_rev
    # Option 2:
    str_rev = list(reversed(string))
    return str_rev == list(string)



#%%
print("palindrome('Madam'):")
print(palindrome("Madam"))
print("palindrome('nurses run'):")
print(palindrome("nurses run"))
print("palindrome('nurse run'):")
print(palindrome("nurse run"))


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

def input_incorrect(user_guess):
    return (len(user_guess) > 1) or (not user_guess.isnumeric())

def guessing_game():
    from random import randint
    num_to_guess = randint(1,9)
    print("This is a guessing game. I'll 'think' of a number and you'll have max 3 attempts to guess what number it is")

    attempt_cnt = 1
    while attempt_cnt <= 3:
        msg = "Guess a number (" + str(attempt_cnt) + ". attempt)\n"
        guess = input(msg)
        if input_incorrect(guess):
            print("Incorrect input! Only single digit numbers are allowed")
            continue
        if int(guess) == num_to_guess:
            print("Congratulations! You've correctly guessed the number")
            return
        attempt_cnt += 1
        feedback = "Incorrect! You can try again" \
            if attempt_cnt <= 3 \
            else "Incorrect! More luck next time. If curious, the number was " + str(num_to_guess)
        print(feedback)




#%%
guessing_game()


#%%
if __name__ == '__main__':

    odd_or_even()

    factorial(7)

    a = [31, 72, 13, 41, 5, 16, 87, 98, 9]
    print("3rd lowest in [31, 72, 13, 41, 5, 16, 87, 98, 9]:")
    print(nth_lowest(a, 3))
    print("6th lowest in ['f', 'r', 't', 'a', 'b', 'y', 'j', 'd', 'c']:")
    print(nth_lowest(['f', 'r', 't', 'a', 'b', 'y', 'j', 'd', 'c'], 6))
    print("2nd lowest in 'today':")
    print(nth_lowest('today', 2))

    print(list_stats([3.4, 5.6, -4.2, -5.6, 9, 1.2, 11.3, -23.45, 81]))

    list_operations([1, 1, 2, 3, 5, 8, 13, 5, 21, 34, 55, 89], 20)

    print("anagrams('School master', 'The classroom'):")
    print(anagrams('School master', 'The classroom'))
    print("anagrams('Dormitory', 'Dirty room'):")
    print(anagrams('Dormitory', 'Dirty room'))
    print("anagrams('Conversation', 'Voices rant on'):")
    print(anagrams('Conversation', 'Voices rant on'))
    print("anagrams('Bob', 'Bill'):")
    print(anagrams('Bob', 'Bill'))

    print("palindrome('madam'):")
    print(palindrome("madam"))
    print("palindrome('nurses run'):")
    print(palindrome("nurses run"))
    print("palindrome('nurse run'):")
    print(palindrome("nurse run"))

    guessing_game()