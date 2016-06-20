# This is my completed exercise for Learn Python The Hard Way Exercise 9
#
# This is slightly modified from the lesson so that I can test things out
# and really solidify what I learned.
#
# EXERCISE 9: Printing, Printing, Printing

# Setting some variables
days = "Mon Tues Wed Thurs Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJune\nJuly\nAug\nSept\nOct\nNov\nDec"

# This line will print the variable 'days'
print "Here are the days: ", days

# This line will print the variable 'months' but the \n will indicate that a new line should be started.
print "Here are the months: ", months

# This line will print out the string literally - so the \n will be ignored.
print "Here are the months: %r" % months

# This line will show the function of the three double-quotes.
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
