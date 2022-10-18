#%%
"""
LAB 2
"""
"""
TASK 1:
Write a function that receives two lists and returns a new list that contains 
only those elements (without duplicates) that appear in both input lists.
"""

def common_elements(l1, l2):
    new_list = []
    for item in l1:
        if (item in l2) and (item not in new_list):
            new_list.append(item)
    return new_list


#%%
def common_elements_v2(l1, l2):
    new_list = [item for item in l1 if item in l2]
    return list(set(new_list))

#%%
# Test the function:
a = [1, 1, 2, 3, 5, 8, 13, 21, 55, 89, 5, 10]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(common_elements_v2(a,b))


#%%

"""
TASK 2:
Write a function that receives 2 lists of the same length and returns a new list 
obtained by concatenating the two input lists index-wise. Example:
Input lists:
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
Output: ['My', 'name', 'is', 'Kelly']
"""
def concat_index_wise(l1, l2):
    new_list = []
    for i in range(0,min(len(l1), len(l2))):
        new_list.append(l1[i] + l2[i])
    return new_list

#%%
def concat_index_wise_v2(l1, l2):
    return [l1[i] + l2[i] for i in range(0,min(len(l1), len(l2)))]

#%%
# Test the function:
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly", "aaa"]
print(concat_index_wise_v2(list1, list2))


#%%

""" 
TASK 3:
Write a function that checks and returns whether a given string is a pangram or not.
Pangrams are sentences or phrases containing every letter of the alphabet at least once 
(for example: "The quick brown fox jumps over the lazy dog")

Hint: ascii_lowercase from the string module can be used to get all letters
"""
def pangram(s):
    from string import ascii_lowercase
    s = s.lower()
    for letter in ascii_lowercase:
        if letter not in s:
            return False
    return True

#%%
def pangram_v2(s):
    from string import ascii_lowercase
    return all([letter in s.lower() for letter in ascii_lowercase])


#%%
# Test the function:
print("The quick brown fox jumps over the lazy dog")
print(pangram_v2("The quick brown fox jumps over the lazy dog"))
print("The quick brown fox jumps over the lazy cat")
print(pangram_v2("The quick brown fox jumps over the lazy cat"))


#%%
"""
TASK 4:
Write a function that receives a string with a mix of lower and upper case letters.
The function arranges letters in such a way that all lowercase letters come first,
followed by all upper case letters. Non-letter characters (if any) are ignored, that is,
not included in the new 're-arranged' string.
The new,'re-arranged' string is the function's return value.
"""
def rearrange_string(s):
    lower_case = [ch for ch in s if ch.islower()]
    upper_case = [ch for ch in s if ch.isupper()]
    # lower_case.extend(upper_case)
    # return "".join(lower_case)
    return "".join(lower_case + upper_case)


#%%
# Test the function:
print("Rearranging string: 'PyNaTive_2021'")
print(rearrange_string("PyNaTive_2021"))

#%%

"""
TASK 5:
Write a function that accepts a sequence of comma separated passwords and
checks their validity using the following criteria:
1. At least 1 letter between [a-z] => At least 1 lower case letter
2. At least 1 number between [0-9] => At least 1 digit
3. At least 1 letter between [A-Z] => At least 1 upper case letter
4. At least 1 of these characters: $,#,@
5. Length in the 6-12 range (including 6 and 12)
Passwords that match the criteria should be printed in one line separated by a comma.
"""
def password_check(candidates):
    candidates = [c.lstrip() for c in candidates.split(",")]
    passwords = []
    for c in candidates:
        valid = [False]*5
        if 6 <= len(c) <= 12:
            valid[4] = True
        else:
            continue
        for ch in c:
            if ch.islower(): valid[0] = True
            elif ch.isdigit(): valid[1] = True
            elif ch.isupper(): valid[2] = True
            elif ch in '#$@': valid[3] = True

        if all(valid):
            passwords.append(c)
    return ", ".join(passwords)


#%%
# Test the function:
print("Passwords to check: ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR")
password_check("ABd1234@1, a F1#, 2w3E*, 2We334#5,t_456WR")

#%%

"""
TASK 6:
Write a function that receives a report (as a string) on the state (up / down) of several servers.
Each line of the report refers to one server, and has the following format:
"Server <server_name> is <up/down>"
Note that some lines may be empty.
Note also that some servers might be mentioned multiple times, in which case, the latest status
should be considered the valid one.
The function should process the report and print:
- the total number of servers mentioned in the report
- the proportion of servers that are down
- names of servers that are down (if any)
"""
def server_status(report):
    lines = [line.lstrip() for line in report.split("\n") if line.lstrip() != ""]
    # lines = [line for line in lines if line != ""]
    all_servers = []
    servers_down = []
    lines.reverse()
    for line in lines:
        _, s_name, _, s_status = line.split()
        if s_name not in all_servers:
            all_servers.append(s_name)
            if s_status == "down":
                servers_down.append(s_name)

    print(f"Total number of servers: {len(all_servers)}")
    print(f"Proportion of servers that are down: {len(servers_down)/len(all_servers):.2f}")
    print("Servers that are down:", ", ".join(servers_down))

#%%
# Test the function:
sample_input = '''
        Server abc01 is up
        Server abc02 is down
        Server xyz01 is down
        Server xyz02 is up
        
        Server abc01 is down
        Server xyz01 is up
        '''
server_status(sample_input)


#%%

"""
TASK 7:
Write a function that finds numbers between 100 and 400 (both included)
where each digit of a number is even. The numbers that match this criterion
should be printed as a comma-separated sequence.
"""


#%%
# Test the function:
# numbers_with_all_even_digits()

#%%

if __name__ == '__main__':
    pass

    # # Task 1:
    # a = [1, 1, 2, 3, 5, 8, 13, 21, 55, 89, 5, 10]
    # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # print(common_elements(a,b))
    #
    # # Task 2:
    # list1 = ["M", "na", "i", "Ke"]
    # list2 = ["y", "me", "s", "lly"]
    # print(concat_index_wise(list1, list2))
    #
    # # Task 3:
    # print("The quick brown fox jumps over the lazy dog")
    # print(pangram("The quick brown fox jumps over the lazy dog"))
    # print("The quick brown fox jumps over the lazy cat")
    # print(pangram("The quick brown fox jumps over the lazy cat"))
    #
    # # Task 4:
    # print(("Rearranging string: 'PyNaTive_2021'"))
    # print(rearrange_string("PyNaTive_2021"))
    #
    # # Task 5:
    # print("Passwords to check: ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR")
    # password_check("ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR")
    #
    # # Task 6:
    # sample_input = '''
    #     Server abc01 is up
    #     Server abc02 is down
    #     Server xyz01 is down
    #     Server xyz02 is up
    #     '''
    # server_status(sample_input)
    #
    # # Task 7:
    # numbers_with_all_even_digits()
