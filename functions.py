# SOLUTIONS!

################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".

def print_hello_world():
    
    """Print 'hello world'"""
    
    print 'hello world'
    
    return

print_hello_world()

# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.

def say_hi_name(name):

    """Take a name as a string and print 'Hi' followed by the name""" 

    print "Hi {}".format(name)
    
    return

say_hi_name('Sarah')

# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.

def get_product(x, y):

    """Take two numbers and multiply them. Print result."""

    print x + y

    return

get_product(2, 3)

# 4. Write a function that takes a string and an integer and
#    prints the string that many times

def print_string_multiple(string, n):
    """Print a string n number of times."""

    print string * n

    return

print_string_multiple('Hip hip hurray! ', 3)

# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".

def print_higher_lower_0(num):
    """Take an integer and print whether that integer is higher or lower than 0"""

    if num > 0:
        print "Higher than zero"
    elif num < 0:
        print "Lower than zero"
    elif num == 0:
        print "Zero"
    
    return

print_higher_lower_0(5)
print_higher_lower_0(-1)

# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def divisible_by_3(num):
    """Take an integer and return a boolean depending on whether number is evenly
    divisible by 3"""

    if num % 3 == 0:
        return True
    else:
        return False

print divisible_by_3(7)
print divisible_by_3(9)

# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.

def return_num_spaces(string):
    """Return the number of spaces in a string of words"""

    num_spaces = 0

    for char in string:
        if char == ' ':
            num_spaces += 1

    return num_spaces

print return_num_spaces('The quick brown fox jumped over the lazy dog.')

# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def calculate_total_paid(price, tip = .15):
    """Return the total mount paid for a meal, given the price of the meal
    and tip amount (default amount is 15%)"""

    return price + (price * tip)

print calculate_total_paid(50)
print calculate_total_paid(50, .2)

# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.
#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.

def return_info(num):
    """Return a list indicating whether an integer is positive or negative and 
    even or odd."""

    if num > 0:
        pos_or_neg = 'Positive'
    elif num < 0:
        pos_or_neg = 'Negative'
    elif num == 0:
        pos_or_neg = 'Zero'

    if num % 2 == 0:
        even_or_odd = 'Even'
    else:
        even_or_odd = 'Odd'

    return [pos_or_neg, even_or_odd]

x = return_info(5)
print x

pos_or_neg, even_or_odd = x
print 'Positive or negative?: {}; Even or odd?: {}'.format(pos_or_neg, even_or_odd)


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
    
    if state == 'CA':
        tax = .07

    total = price + (price * tax)

    return "Cost of item plus tax in {}: ${:.2f}".format(state, total)

print get_item_cost(20, 'CA')
print get_item_cost(state='NH', price=20)


# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.

def return_title_and_name(name, job_title = "Engineer"):

    return "{} {}".format(job_title, name)

print return_title_and_name('Bob', 'Nurse')
print return_title_and_name('Sarah')

# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

def write_letter(receiver_name, sender_name, receiver_title = "Engineer"):
    
    title_and_name = return_title_and_name(receiver_name, receiver_title)

    return "Dear {}, I think you are amazing! Sincerely, {}".format(title_and_name, 
            sender_name)

print write_letter('Sarah', 'Joe')
print write_letter(receiver_title = 'Doctor', receiver_name = 'Jon', sender_name = 'Delilah')


# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.

def append_number(num):
    
    numbers = [1,2]

    numbers.append(num)

    print numbers
    return

append_number(60)