# SOLUTIONS!

################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".

def print_hello_world():
    
    """Print 'hello world

        For example:

        >>> print_hello_world()
        hello world

    '"""
    
    print 'hello world'
    
    return


# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.

def say_hi_name(name):

    """Take a name as a string and print 'Hi' followed by the name

        For example:

        >>> say_hi_name('Joan')
        Hi Joan

    """ 

    print "Hi {}".format(name)
    
    return


# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.

def get_product(x, y):

    """Take two numbers and multiply them. Print result.

        For example:

        >>> get_product(5, 5)
        10

    """

    print x + y

    return

# 4. Write a function that takes a string and an integer and
#    prints the string that many times

def print_string_multiple(string, n):
    """Print a string n number of times.

        For example:

        >>> print_string_multiple('blue', 5)
        blueblueblueblueblue

    """

    print string * n

    return


# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".

def print_higher_lower_0(num):

    """Take an integer and print whether that integer is higher or lower than 0

        For example:

        >>> print_higher_lower_0(4)
        Higher than zero

        >>> print_higher_lower_0(-3)
        Lower than zero

        >>> print_higher_lower_0(0)
        Zero


    """

    if num > 0:
        print "Higher than zero"
    elif num < 0:
        print "Lower than zero"
    elif num == 0:
        print "Zero"
    
    return


# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def divisible_by_3(num):
    """Take an integer and return a boolean depending on whether number is evenly
    divisible by 3.

        For example:

        >>> divisible_by_3(7)
        False

        >>> divisible_by_3(9)
        True

    """

    if num % 3 == 0:
        return True
    else:
        return False


# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.

def return_num_spaces(string):
    """Return the number of spaces in a string of words.

        For example:

        >>> return_num_spaces('I like pizza.')
        2

        >>> return_num_spaces('I  love  double  spaces.')
        6

    """

    # start the counting variable at 0
    num_spaces = 0

    # loop through each character in the string and increase counting variable
    # when loop encounters a space.
    for char in string:
        if char == ' ':
            num_spaces += 1

    return num_spaces

# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def calculate_total_paid(price, tip = .15):
    """Return the total mount paid for a meal, given the price of the meal
    and tip amount (default amount is 15%).

        For example:

        >>> calculate_total_paid(10)
        11.5

        >>> calculate_total_paid(200, .2)
        240.0
    """

    return float(price + float((price * tip)))

# test cases
# print "${:,.2f}".format(calculate_total_paid(50))
# print "${:,.2f}".format(calculate_total_paid(50, .2))

# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.
#
#   Then, write code that shows the calling of this function
#   on a number and unpack what is returned into two
#   variables --- sign and parity (whether it's positive
#   or negative). Print sign and parity.

def return_info(num):
    """Return a list indicating whether an integer is positive or negative and 
    even or odd.

        For example:

        >>> return_info(5)
        ['Positive', 'Odd']

        >>> return_info(-4)
        ['Negative', 'Even']

    """

    # test whether integer is positive or negative 
    if num > 0:
        pos_or_neg = 'Positive'
    elif num < 0:
        pos_or_neg = 'Negative'
    elif num == 0:
        pos_or_neg = 'Zero'

    # then test whether integer is even or odd
    if num % 2 == 0:
        even_or_odd = 'Even'
    else:
        even_or_odd = 'Odd'

    # return a list containing the information
    return [pos_or_neg, even_or_odd]

# call the function for the integer 5
# x = return_info(5)
# print x

# unpack the returned list
# pos_or_neg, even_or_odd = x

# print the results of the unpacking
# print 'Positive or negative?: {}; Even or odd?: {}'.format(pos_or_neg, even_or_odd)


################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.

def get_item_cost(price, state, tax = .05):

    """
    Return the cost of an item plus tax depending upon the state passed to the 
    function. Default tax is 5%, but if 'CA' is entered as an argument, the tax 
    amount becomes 7%. The user may also indicate a different tax amount, or
    leave that argument out and resort to the default.

        For example:

        >>> get_item_cost(20, 'CA')
        Cost of item plus tax in CA: $21.40
        21.4

        >>> get_item_cost(state='NH', price=20)
        Cost of item plus tax in NH: $21.00
        21.0

        >>> get_item_cost(1500, 'CA', .08)
        Cost of item plus tax in CA: $1,620.00
        1620.0

        >>> get_item_cost(1500, 'CA')
        Cost of item plus tax in CA: $1,605.00
        1605.0

    """
    
    # check if 'CA' was given as an argument
    if state == 'CA' and tax == .05:
        tax = .07

    total = float(price + float((price * tax)))

    print "Cost of item plus tax in {}: ${:,.2f}".format(state, total)
    return total

# 2. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name.

def return_title_and_name(name, job_title = "Engineer"):

    """
    Return a person's job title and name. Default job is Engineer, but user
    can call function using a different title argument.

        For example:

        >>> return_title_and_name('Sarah')
        'Engineer Sarah'

        >>> return_title_and_name('Bob', 'Nurse')
        'Nurse Bob'

    """

    title_and_name = "{} {}".format(job_title, name)

    return title_and_name


# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

def write_letter(receiver_name, sender_name, receiver_title = "Engineer"):
    
    """
    Print a letter given a receiver's name, receiver's job title and sender's name.
    Based on function return_title_and_name. Default title is Engineer unless
    otherwise specified.

        For example:

        >>> write_letter('Sarah', 'Joe')
        Dear Engineer Sarah, I think you are amazing! Sincerely, Joe

        >>> write_letter(receiver_title = 'Doctor', receiver_name = 'Jon', sender_name = 'Delilah')
        Dear Doctor Jon, I think you are amazing! Sincerely, Delilah

    """

    # call the return_title_and_name function
    title_and_name = return_title_and_name(receiver_name, receiver_title)

    # print the letter
    print "Dear {}, I think you are amazing! Sincerely, {}".format(title_and_name, 
            sender_name)
    return

# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.

def append_number(num):
    """
    Append a number (called in the function) to a list of numbers (already defined
    within the function).

        For example: 

        >>> append_number(50)
        [1, 2, 50]

    """

    numbers = [1,2]

    numbers.append(num)

    print numbers
    return


###
if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED"
    print