#%%
"""
LAB 4
"""
from functools import reduce

#%%
"""
TASK 1:
Write the 'compute_product' function that receives an arbitrary number of numeric values and computes their product. 
The function also receives a named argument "absolute" with the default value False, which 
determines if the numeric values should be used as given or their absolute value should be used instead.

Implement the function in two different ways:
1) using a for loop
2) using the reduce() f. from the functools module together with an appropriate lambda f.
For an example and explanation of reduce() f. check, for example, these articles:
- https://realpython.com/python-reduce-function/
- https://www.python-course.eu/python3_lambda.php
"""

def compute_product(*numbers, absolute=False):
    # Option 1
    # p = 1
    # for num in numbers:
    #     p *= abs(num) if absolute else num
    # return p
    # Option 2
    return reduce(lambda a,b: a*b, [abs(num) if absolute else num for num in numbers])


#%%
# Test the function

# print(compute_product(1,-4,13,2))
# print(compute_product(1, -4, 13, 2, absolute=True))
# print()

# # Calling the compute_product function with a list
# num_list = [2, 7, -11, 9, 24, -3]
# # This is NOT a way to make the call:
# print("Calling the function by passing a list as the argument")
# print(compute_product(num_list))
# print()
# # instead, this is how it should be done (the * operator is 'unpacking' the list):
# print("Calling the function by passing an UNPACKED list as the argument")
# print(compute_product(*num_list))


#%%

"""
TASK 2:
Write the 'select_strings' function that receives an arbitrary number of strings and returns a list 
of those strings where the first and the last character are the same (case-insensitive) and the total 
number of unique characters is above the given threshold. The threshold is the function's named argument 
with the default value of 3.

Implement the function in three different ways:
1) using the for loop
2) using list comprehension
3) using the filter() f. together with an appropriate lambda f.
"""

def select_strings(*strings, threshold=3):
    # Option 1
    # selection = list()
    # for s in strings:
    #     if s.lower()[0]==s.lower()[-1] and len(set(s)) > threshold:
    #         selection.append(s)
    # return selection
    # Option 2
    # return [s for s in strings if s.lower()[0]==s.lower()[-1] and len(set(s)) > threshold]
    # Option 3
    return list(filter(lambda s: (s.lower()[0]==s.lower()[-1]) and (len(set(s)) > threshold), strings))


#%%
# Test the function:
# str_list = ['yellowy', 'Bob', 'lovely', 'Yesterday', 'too']
# print(select_strings(*str_list))

#%%

"""
TASK 3:
Write the 'process_product_orders' function that receives a list of product orders, 
where each order is a 4-tuple of the form (order_id, product_name, quantity, price_per_item). 
The function returns a list of 2-tuples of the form (order_id, total_price) where total price 
(in USD) for an order is the product of the quantity and the price per item (in USD).
The function also receives two named arguments that may affect the computed total price:
- discount - the discount, expressed in percentages, to be applied to the total price;
  the default value of this argument is None
- shipping - the shipping cost to be added to orders with total price less than 100 USD; 
  the default value of this argument is 10 (USD).

Implement the function in three different ways:
1) using the for loop
2) using list comprehension
3) using the map() f. together with an appropriate auxiliary function
"""

def process_product_orders(orders, discount=None, shipping=100):
    def apply_discount(price):
        return price * (1-discount/100) if discount else price
    # Option 1
    # processed_orders = list()
    # for id, _, quantity, item_price in orders:
    #     tot_price = apply_discount(item_price) * quantity
    #     tot_price += shipping if tot_price < 100 else 0
    #     processed_orders.append((id, tot_price))
    # return processed_orders
    # Option 2
    # processed_orders = [(id, quantity * apply_discount(item_price)) for id, _, quantity, item_price in orders]
    # return [(id, tot_price) if tot_price >= 100 else (id, tot_price+shipping) for id, tot_price in processed_orders]
    # Option 3
    def process_order(order):
        id, _, quantity, item_price = order
        tot_price = apply_discount(item_price) * quantity
        return (id, tot_price + shipping) if tot_price < 100 else (id, tot_price)
    return list(map(process_order, orders))


#%%
# Test the function:
# orders = [("34587", "Learning Python, Mark Lutz", 4, 40.95),
#           ("98762", "Programming Python, Mark Lutz", 5, 56.80),
#           ("77226", "Head First Python, Paul Barry", 3, 32.95),
#           ("88112", "Einführung in Python3, Bernd Klein", 3, 24.99)]
#
# print(process_product_orders(orders))
# print()
# print("The same orders with discount of 10%")
# print(process_product_orders(orders, discount=10))

#%%

"""
TASK 4:
Create a decorator ('timer') that measures the time a function takes to execute and 
prints the duration to the console.

Hint 1: use the decorator-writing pattern:
import functools
def decorator(func):
     @functools.wraps(func)	 # preserves func's identity after it's decorated
     def wrapper_decorator(*args, **kwargs):
         # Do something before
         value = func(*args, **kwargs)
         # Do something after
         return value
     return wrapper_decorator

Hint 2: to measure the time of function execution, use the perf_counter() f.
from the time module (it returns a float value representing time in seconds).
"""
import functools
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        from time import perf_counter
        start_time = perf_counter()
        value = func(*args, **kwargs)
        duration = perf_counter() - start_time
        print(f"Function {func.__name__} completed in {duration:.4f} seconds")
        return value
    return wrapper_timer

#%%

"""
TASK 4.1
Write the 'compute_sum' function that for each number x in the range 1..n (n is the input parameter)
computes the sum: S(x) = 1 + 2 + ... + x-1 + x, and returns the sum of all S(x).
Decorate the function with the timer decorator.

Write the function in a few different ways - e.g. (1) using a loop; (2) using list comprehension;
(3) using the map f. - and decorate each one with the timer to compare their performance
"""

@timer
def compute_sum_loop(n):
    tot_sum = 0
    for x in range(1,n+1):
        for i in range(1,x+1):
            tot_sum += i
    return tot_sum

@timer
def compute_sum_lc(n):
    return sum([sum(range(1,x+1)) for x in range(1,n+1)])

@timer
def compute_sum_map(n):
    # Option 1
    return sum(map(lambda x: sum(range(1,x+1)), range(1, n+1)))


#%%
# Test the function:
# print(compute_sum_loop(10000))
# print()
# print(compute_sum_lc(10000))
# print()
# print(compute_sum_map(10000))

#%%
"""
TASK 4.2
Write the 'mean_median_diff' function that creates a list by generating n random numbers (integers) 
between 1 and k (n and k are the function's input parameters). After generating and adding each number 
to the list, the function computes and prints the difference between mean and median of the list elements. 
Decorate the function with the timer decorator.

Bonus: assure that each function invocation produces the same results
"""
@timer
def mean_median_diff(n, k):
    from random import randint, seed
    from statistics import mean, median

    rand_list = list()
    seed(1)
    for i in range(n):
        num = randint(1, k)
        rand_list.append(num)
        print(f"After adding {num} to the list, the mean-median difference is {abs(mean(rand_list) - median(rand_list))}")


#%%
# Test the function:
# mean_median_diff(100, 250)


#%%
"""
TASK 5:
Create a decorator ('standardiser') that standardizes (= z-transforms) a list of numbers before passing 
the list to the decorated function for further computations. The decorator also rounds the computation 
result to 4 digits before returning it (as its return value).

Bonus: before calling the decorated function, print, to the console, its name with the list of input 
parameters (after standardisation)
"""

def standardiser(func):
    @functools.wraps(func)
    def wrapper_standardiser(*args, **kwargs):

        from statistics import mean, stdev
        if all([isinstance(a, (int, float)) for a in args]):
            m = mean(args)
            sd = stdev(args)
            args = [(a-m)/sd for a in args]
        else:
            print("The function's input are not numbers, and thus cannot be standardised")

        f_str = f"Function {func.__name__} with input parameters:\n"
        f_str += f"\t- args: {','.join([str(round(a, 4)) for a in args])}\n"
        if kwargs:
            f_str += f"\t- kwargs: {','.join([k + '=' + str(v) for k,v in kwargs.items()])}"
        print(f_str)

        value = func(*args, **kwargs)

        value = round(value, ndigits=4)

        return value

    return wrapper_standardiser

#%%
"""
TASK 5.1:
Write the 'sum_of_sums' function that receives an arbitrary number of int values and 
for each value (x) computes the following sum:
S(x) = 1 + x + x**2 + x**3 + ... + x**n
where n is a named argument with default value 10.
The function returns the sum of S(x) of all received int values.
Decorate the function with the standardise decorator.
"""

@standardiser
def sum_of_sums(*numbers, n=10):
    # Option 1
    # tot_sum = 0
    # for x in numbers:
    #     tot_sum += sum([x**i for i in range(n+1)])
    # return tot_sum
    # Option 2
    # def sum_of_x(x):
    #     return sum([x**i for i in range(n+1)])
    # return sum(map(sum_of_x, numbers))
    # Option 3
    return sum([sum([x**i for i in range(n+1)]) for x in numbers])


#%%
# Test the function:
# print(sum_of_sums(1,3,5,7,9,11,13, n=7))


#%%

if __name__ == '__main__':

    pass

    # Task 1
    # print(compute_product(1,-4,13,2))
    # print(compute_product(1, -4, 13, 2, absolute=True))
    # print()
    # # Calling the compute_product function with a list
    # num_list = [2, 7, -11, 9, 24, -3]
    # # This is NOT a way to make the call:
    # print("Calling the function by passing a list as the argument")
    # print(compute_product(num_list))
    # print()
    # # instead, this is how it should be done (the * operator is 'unpacking' the list):
    # print("Calling the function by passing an UNPACKED list as the argument")
    # print(compute_product(*num_list))
    # print()

    # Task 2
    # str_list = ['yellowy', 'Bob', 'lovely', 'Yesterday', 'too']
    # print(select_strings(*str_list))
    # print()

    # Task 3
    # orders = [("34587", "Learning Python, Mark Lutz", 4, 40.95),
    #           ("98762", "Programming Python, Mark Lutz", 5, 56.80),
    #           ("77226", "Head First Python, Paul Barry", 3, 32.95),
    #           ("88112", "Einführung in Python3, Bernd Klein", 3, 24.99)]
    #
    # print(process_product_orders(orders))
    # print()
    # print("The same orders with discount of 10%")
    # print(process_product_orders(orders, discount=10))
    # print()

    # Task 4.1
    # print(compute_sum_loop(10000))
    # print()
    # print(compute_sum_lc(10000))
    # print()
    # print(compute_sum_map(10000))
    # print()

    # Task 4.2
    # mean_median_diff(100, 250)
    # print()

    # Task 5.1
    # print(sum_of_sums(1,3,5,7,9,11,13, n=7))


