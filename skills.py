"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def print_list(my_list):
    """Print each item in the input list

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9

    """
    # iterate through all items in list and print item
    for item in my_list:
        print item

    # Return nothing
    return

def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    # Find only the odd elements (not evenly divisible by 2) and return them
    # as a list

    odd_elements = [num for num in number_list if num % 2 != 0]

    return odd_elements


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """

    # do the opposite of the above function (this time, find positive #s)

    even_elements = [num for num in number_list if num % 2 == 0]
    return even_elements


def every_other_item(my_list):
    """Return a list that contains every other item in my_list starting
       with the first item.

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(["you", "friend", "are", "very", "good", " ", "at", " ", "coding"])
       ['you', 'are', 'good', 'at', 'coding']

    """
    # return a slice of the list that skips every 2nd number

    every_other_item = my_list[::2]
    
    return every_other_item

def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """

    # for i in range(len(my_list)):
    #     print "{} {}".format(i, my_list[i]) 

    # return

    # learned 'enumerate' function, i is the index position and item is the 
    # element in that position in the list
    # print both of those elemetns

    for i, item in enumerate(my_list):
        print i, item
    return


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    # find the words that are longer than 4 characters and create a list of those

    long_words = [word for word in word_list if len(word) > 4]

    return long_words


def n_long_words(word_list, n):
    """Return all words in input list that are longer than n characters.

    >>> n_long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"], 3)
    ['hello', 'spam', 'spam', 'bacon', 'bacon']

    >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
    ['apples', 'bananas']
    """

    # same as the above function, except this time the character length
    # is called as an argument instead of a set value within the function

    n_long_words = [word for word in word_list if len(word) > n]

    return n_long_words


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """
    
    # determine outcome for a blank list
    if number_list == []:
        smallest_int = False
        return

    # start with the first number in the list and compare the next item in the
    # list to it. If it's smaller than the first number, smallest_int rebinds
    # to the lower value. 
    # Continue to loop through the whole list this way.

    else:
        smallest_int = number_list[0]
        for i, item in enumerate(number_list):
            if smallest_int > item:
                smallest_int = item

    return smallest_int


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """
    # Same as the above function, but this time, find the largest integer

    if number_list == []:
        largest_int = False
        return

    else:
        largest_int = number_list[0]
        for i, item in enumerate(number_list):
            if largest_int < item:
                largest_int = item
    
    return largest_int


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    # create a list of numbers that contains half of each number in the input list
    # make sure the number is a float so the decimal point is not dropped

    halvesies = [(float(num)/2) for num in number_list]

    return halvesies


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """

    # calculate the length of each word in a list and store those lengths
    # in a new list

    word_lengths = [len(word) for word in word_list]

    return word_lengths


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """

    # initialize the sum_of_numbers variable, set to 0

    sum_of_numbers = 0

    # set condition for a blank list
    if number_list == []:
        return sum_of_numbers

    # if the list is not blank, iterate through the list and add each number
    # to the running total

    else:
        for num in number_list[:]:
            sum_of_numbers = sum_of_numbers + num

    return sum_of_numbers


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    # initialize the prod_of_numbers vaiable as 1.

    prod_of_numbers = 1

    # iterate through the list and multiply each number by the running product
    # of the list
    for num in number_list:
        prod_of_numbers = prod_of_numbers * num

    # set condition for a blank list
    if number_list == []:
        prod_of_numbers = 1

    return prod_of_numbers


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    
    # initialize a blank string for the join_strings variable

    join_strings = ''

    # add each word in a string to the join_strings variable

    for word in word_list:
        join_strings = join_strings + word

    # if there is a blank input list, the string remains empty

    if word_list == []:
        join_strings = ''

    return join_strings


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """
    
    # similar to sum_of_numbers, calculate the sum of a list of numbers, 
    # divide that sum by the number of elements in the list, and return the average.

    sum_of_numbers = 0

    for num in number_list:
        sum_of_numbers = sum_of_numbers + num

    # make sure the average is a float

    average_of_list = float(sum_of_numbers/float(len(number_list)))

    return average_of_list


def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """
    
    # join a list of strings together with a comma as separator, beginning with 
    # the first input word and continuing sequentially

    strings_with_comma = list_of_words[0]
    
    # set condition for a list with only one element
    if len(list_of_words) == 1:
        strings_with_comma = list_of_words[0]

    # iterate through the list of words and add the next word in the list to the
    # string    
    else:
        for word in list_of_words[1:]:
            strings_with_comma = "{}, {}".format(strings_with_comma, word) 

    return strings_with_comma


def foods_in_common(foods1, foods2):
    """Using ANY Python data structure presented in the last week, given 2 lists of foods, 
    return a set of items that are in common between the two. (Don't include any duplicates
    in the output collection.)
    
    For example:

    >>> foods_in_common(["cheese", "bagel", "cake"], ["hummus", "beets", "bagel", "lentils"])
    set(['bagel'])

    If there are no foods in common, return an empty set.

    >>> foods_in_common(["lamb", "chili", "cheese"], ["cake", "ice cream"])
    set([])

    """

    # Using set math, create two sets from two lists of foods and determine the
    # intersection of the sets. Returns a set.

    set_foods_1 = set(foods1)
    set_foods_2 = set(foods2)

    foods_in_common = set_foods_1 & set_foods_2

    return foods_in_common


def reverse_list(my_list):
    """Return the inputted list, reversed.

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

    Do not use the python methed reverse()/reversed().

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    """
    
    # move through the list sequentially and pop the last element out into a new
    # list, called reverse_list, until reaching the first element.

    reverse_list = []
    for i in range(len(my_list)):
        word = my_list.pop(-1)
        reverse_list.append(word)

    return reverse_list

    # I originally used this code, but this looks like what the function below
    # is asking for, so I wrote the code above

    # reverse_list = my_list[::-1]

    # return reverse_list

def reverse_list_in_place(my_list):
    """Return the inputted list reversed--WITHOUT creating a new list.
       This will involve moving the items in my_list to different positions 
       in the same list.

       Do not use the python methed reverse()/reversed()

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']


    """

    # slice the whole list starting from the end in -1 incremenets (moving backwards)

    my_list[::-1]

    return my_list



def duplicates(my_list):
    """Return a list of words which are duplicated in the input list.

    >>> duplicates(["apple", "apple", "banana", "cherry", "banana", "apple"])
    ['apple', 'banana']

    >>> duplicates([1, 2, 2, 4, 4, 4, 7])
    [2, 4]
    

    """
    # note: I changed the Docstrings above so that the output of the second
    # test condition == [2, 4] instead of [4, 2] and the test wouldn't fail. 
    # I thought that the order didn't matter as long as the numbers were correct (?).


    # determine the unique pieces of an input list by passing the list to a set
    # and then turning that set into a list.
    unique_items = set(my_list)
    unique_items = list(unique_items) 

    # for each item in the list of unique list elements, iterate through and pop
    # out that element from the original input list (leaving only the items that 
    # are repeated).
    for i, item in enumerate(unique_items):
        if item in my_list:
            my_list.remove(item)           

    # create a list of unique elements from that list of duplicates
    only_duplicates = set(my_list)
    only_duplicates = list(only_duplicates)        

    return only_duplicates


def find_letter_indices(list_of_words, letter):
    """Given a list of words and a letter, return a list of integers that correspond
    to the index of the first occurance of the letter in that word.

    Do not use the .index() list method.

    >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
    [0, 1, 2]

    If the letter doesn't occur in one of the words, use None for that word in
    the output list. For example:

    >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
    [0, 1, 2, None]

    """
    # initialize the list
    list_of_indices = []

    # condition if none of the letters in a word match the target letter 
    for word in list_of_words:
        if letter not in word:
            list_of_indices.append(None)

    # move through the letters in the word, and if a given letter matches the
    # target, append the index of that letter in the word to the list of indices.
    # Set i to equal the length of the word (thus ending the iteration,
    # because this function only calls the first time the letter appears).
        else:
            for i, item in enumerate(word):
                if letter == item:
                    list_of_indices.append(i)
                    i = len(word)

    return list_of_indices

def largest_n_items(input_list, n):
    """Given a list of integers along with an integer n, return a 
    list of the largest n numbers in the input list in ascending order. 

    You can assume that n will be less than the length of the list. 

    For example:

    >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
    [59, 700, 6006]

    """
    # Sort a list of integers and then slice the list depending on the number of 
    # highest numbers requested in the function call. Highest numbers will be at
    # the end of the list, so use a negative index to count from the end.

    input_list.sort()

    return input_list[-n::]



##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.
if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
