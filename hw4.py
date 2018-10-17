"""
CS 196 FA18 HW4
Prepared by Andrew, Emilio, and Prithvi

You might find certain default Python packages immensely helpful.
"""

# Good luck!

from collections import Counter

"""
most_common_char

Given an input string s, return the most common character in s.
"""
def most_common_char(s):
    if s == "":
        return "error: empty string does not have any characters"
    else:
        dict = {}
        common = Counter(s).most_common(len(s))
        for elem in common:
            dict[elem[0]] = elem[1]
        # print(dict)

        #  a list of the # of occurrences of chars in string in order of greatest occurrence to least occurrence
        lis_of_occurrences = []
        for y in dict.items():
            lis_of_occurrences.append(y[1])
        # print(lis_of_occurrences)

        # finds the max # of occurrence in lis_of_occurrences
        maxNum = lis_of_occurrences[0]

        # a list of the most common chars in string --> returns any one of the elements in this list
        lis_of_common_char = []
        for x in dict:
            if dict[x] == maxNum:
                lis_of_common_char.append(x)
        # print(lis_of_common_char)

        # returns most common char in string
        return lis_of_common_char[0]


"""
alphabet_finder

Given an input string s, return the shortest prefix of s (i.e. some s' = s[0:i] for some 0 < i <= n)
that contains all the letters of the alphabet.
If there is no such prefix, return None.
Your function should recognize letters in both cases, i.e. "qwertyuiopASDFGHJKLzxcvbnm" is a valid alphabet.

Example 1:
    Argument:
        "qwertyuiopASDFGHJKLzxcvbnm insensitive paella"
    Return:
        "qwertyuiopASDFGHJKLzxcvbnm"

Example 2:
    Argument:
        "aardvarks are cool!"
    Return:
        None
"""
def alphabet_finder(s):
    # creates an alphabet dictionary with all values set to 0
    alpha_dict = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        alpha_dict[letter] = 0
    # print(alpha_dict)

    # makes all letters in the string lowercase
    s = s.lower()
    # print(s)

    # creates a list of all possible prefixes of the string
    prefix_lis = s.split()
    # print(prefix_lis)

    # creates a list of all the prefixes that has 26 letters (alphabet has 26 letters)
    valid_prefixes = []
    for elem in prefix_lis:
        if len(elem) == 26:
            valid_prefixes.append(elem)
    # print(valid_prefixes)

    # returns shortest prefix that contains all letters of the alphabet only once. if none exist, returns None
    for elem in valid_prefixes:
        for letter in elem:
            alpha_dict[letter] = 0
            alpha_dict[letter] += 1
        # print(alpha_dict)
        if all(value == 1 for value in alpha_dict.values()) == True:
            return elem
        else:
            continue
    # print(alpha_dict)
    if all(value == 0 for value in alpha_dict.values()) == True:
        return None


"""
longest_unique_subarray

Given an input list of integers arr,
return a list with two values [a,b] such that arr[a:a+b] is the longest unique subarray.
That is to say, all the elements of arr[a:a+b] must be unique,
and b must be the largest value possible for the array.
If multiple such subarrays exist (i.e. same b, different a), use the lowest value of a.

Example:
    Argument:
        [1, 2, 3, 1, 4, 5, 6]
    Return:
        [1, 6]
"""
def longest_unique_subarray(arr):
    pass


"""
string_my_one_true_love

A former(?) CA for this course really like[d] strings that have the same occurrences of letters.
This means the staff member likes "aabbcc", "ccddee", "abcabcabc", etcetera.

But the person who wrote all of your homework sets wants to trick the staff with really long strings,
that either could be the type of string that the staff member likes,
or a string that the CA would like if you remove exactly one character from the string.

Return True if it's a string that the homework creator made, and False otherwise.
Don't treat any characters specially, i.e. 'a' and 'A' are different characters.

Ungraded food for thought:
Ideally, your method should also work on integer arrays without any modification.

Example 1:
    Argument:
        "abcbabcdcdda"
        There are 3 a's, 3 b's, 3 c's, and 3 d's. That means it is a very likable string!
    Return:
        True

Example 2:
    Argument:
        "aaabbbcccddde"
        There are 3 a's, 3 b's, 3 c's, and 3 d's. We have 1 e, which we can remove.
    Return:
        True

Example 3:
    Argument:
        "aaabbbcccdddeeffgg"
        This string is similar to the other ones, except with 2 e's, f's and g's at the end.
        To make this string likable, we need to remove the 2 e's, f's, and g's or we can remove
        one a, b, c, and d. However all of these require more than one removal, so it becomes invalid.
    Return:
        False
"""
def string_my_one_true_love(s):
    cnt = Counter()
    for letter in s:
        cnt[letter] += 1
    dict1 = {}
    for x, y in cnt.items():
        dict1[x] = y
    print(dict1)


"""
alive_people

You are given a 2-dimensional list data. Each element in data is a list [birth_year, age_of_death].
Assume that the person was alive in the year (birth_year + age_of_death).
Given that data, return the year where the most people represented in the list were alive.
If there are multiple such years, return the earliest year.

Example:
    Argument:
        [[1920, 80], [1940, 22], [1961, 10]]
    Return:
        1961
"""
def alive_people(data):
    dict2 = {}
    for elem in data:
        dict2[elem[0]] = elem[0] + elem[1]
    # print(dict2)

    # find the max of the birth year, then the min of the death year. the answer is between those values

    # max of birth year
    birth_year = []
    for x in dict2.items():
        birth_year.append(x[0])
    # print(birth_year)
    birth_year.sort(key=int, reverse=True)
    # print(birth_year)
    max_birth_year = birth_year[0]
    #mprint(max_birth_year)

    # min death year
    death_year = []
    for y in dict2.values():
        death_year.append(y)
    # print(death_year)
    death_year.sort()
    # print(death_year)
    min_death_year = death_year[0]
    # print(min_death_year)

    if max_birth_year == min_death_year:
        return "invalid"
    else:
        return max_birth_year


"""
three_sum

Given an input list of integers arr, and a constant target t,
is there a triplet of distinct elements [a,b,c] so that a + b + c = t?

Return a 2-dimensional list of all the unique triplets as defined above.
Each inner list should be a triplet as we defined above.
We don't care about the order of triplets, nor the order of elements in each triplet.

Example:
    Arguments:
        [-1, 0, 1, 2, -1, -4], 0
    Return:
        [
            [-1, 0, 1],
            [-1, -1, 2]
        ]
"""
def three_sum(arr, t):
    pass


"""
happy_numbers

Given an input integer n > 0, return the number of happy integers between 1 and n, bounds inclusive.
https://en.wikipedia.org/wiki/Happy_number

Example 1:
    Argument:
        8
        The happy numbers between 1 and 8 are 1 and 7 (7 -> 49 -> 97 -> 130 -> 10 -> 1)
    Return:
        2468 // 1234 (i.e., 2)
Example 2:
    Argument:
        15
    Return:
        4294967296 ** (1 / 16) (i.e., 4)
"""
def happy_numbers(n):
    pass


"""
zero_sum_subarray

Given an input list of integers arr,
return a list with two values [a,b] such that sum(arr[a:a+b]) == 0.
In plain English, give us the location of a subarray of arr that starts at index a
and continues for b elements, so that the sum of the subarray you indicated is zero.
If multiple such subarrays exist, use the lowest valid a, and then lowest valid b,
in that order of priority.
If no such subarray exists, return None.

Ungraded food for thought:
Think about how to generalize your solution to any arbitrary target sum.

Example 1:
    Argument:
        [0, 1, 2, 3, 4, 5]
        Clearly, the first element by itself forms a subarray with sum == 0.
    Return:
        [0, 1]

Example 2:
    Argument:
        [10, 20, -20, 3, 21, 2, -6]
        In this case, arr[1:3] = [20, -20], so there is a zero sum subarray.
    Return:
        [1, 2]
"""
def zero_sum_subarray(arr):
    pass



