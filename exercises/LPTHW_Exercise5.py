# This is my completed exercise for Learn Python The Hard Way Exercise 5
#
# This is slightly modified from the lesson so that I can test things out
# and really solidify what I learned.
#
# EXERCISE 5: More variables and printing

# -------------------------------------------------------------------------
# Setting the variables
# -------------------------------------------------------------------------
# Setting my name to personalize this exercise
# I'm using double quotes around the last value to see if there is any difference (none that I can see)
my_name = 'Bossy Jossy'
my_age = 29 # yes, 29 again!
my_height = 60 #inches - I'm not going to be in the WNBA.
# my_weight = ? yeah...is Zed serious?  I'm commenting this out  :)
my_eyes = 'brown'
my_teeth = 'white'
my_hair = "brown"


# -------------------------------------------------------------------------
# Summary of the data
# -------------------------------------------------------------------------
# This is covered in a later lesson, but I am going to take notes here as I want to better 
# understand these operators.
#
# String Formatting Operations used in this exercise:
# %s = uses the 'str' function and inserts the presentation string representation (i.e. contents of the string)
# %r = uses the 'repr' function and inserts the literal representation of a string (includes quotes etc)
# %d formts a number for display
#
# Also demonstrated in this lesson are multiple variables.  
#
print "Let's talk about %s." % my_name
print "She is %d inches tall." % my_height
# print "She is %d pounds heavy." % my_weight
# print "Actually, that's not too heavy."
print "She has %s eyes and %s hair." % (my_eyes, my_hair)
print "Her teeth are usually %s - depending on how much coffee she has had!  :) " % my_teeth
print "If I add %d and %d, I get %d." % (my_age, my_height, my_age + my_height)

# Playing around with multiple varibles a bit more
(my_coffee, my_coffee_brewing_method, my_coffee_roast) = 'Starbucks Veranda', "French Press", 'light'
print "My name is %s and I love %s because it is a %s roast which I brew via %s" % (my_name, my_coffee, my_coffee_roast, my_coffee_brewing_method)
