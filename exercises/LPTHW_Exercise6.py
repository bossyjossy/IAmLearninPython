# This is my completed exercise for Learn Python The Hard Way Exercise 6
#
# This is slightly modified from the lesson so that I can test things out
# and really solidify what I learned.
#
# EXERCISE 6: Strings and Text

# Setting variable 'x' to a string.  Also using string formatting operation to format a number within the string.
x = "There are %d types of people..." % 10

# Setting two other variables with string values
binary = "binary"
do_not = "don't"

# Using multiple variables within setting variable 'y'
y = "Those who know %s and those who %s." % (binary, do_not)

# Print these two variables.
print x
print y

# Print these two variables with other string formatting operations.
# The first line should print everything including all quotes.
print "I said: %r." % x
# This line should print just the contents with no quotes.
print "I also said: %s." % y
# This line should print just the contents with single quotes.
print "I also said: '%s'." % y

# More examples
# In this line, the variable is being set to the boolean value of "False"
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious

# If I wanted to set the variable to a string, I would do this:
hilarious2 = "Not!"
joke_evaluation2 = "Isn't that joke so funny?! %s"  #Note: I had to use double quotes because of the contraction
print joke_evaluation2 % hilarious2

# One more example to show connecting two variables which are strings.
w = "This is the left side of ..."
e = " a string with a right side."
print w + e