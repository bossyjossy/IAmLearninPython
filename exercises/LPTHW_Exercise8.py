# This is my completed exercise for Learn Python The Hard Way Exercise 8
#
# This is slightly modified from the lesson so that I can test things out
# and really solidify what I learned.
#
# EXERCISE 8: Printing, Printing

# This line will set the variable 'formatter' to print a string four times
formatter = "%r %r %r %r"

# This section will use the variable with various sets of strings and print them.
# This line will print:  1 2 3 4
print formatter % (1, 2, 3, 4)

# This line will print the numbers spelled out with the quotes with no commas to separate the values.
print formatter % ("one", "two", "three", "four")

# This line will print the four boolean values with no commas to separate the values.
print formatter % (True, False, False, True)

# This line will print '%r %r %r %r' four times (with the single quotes) with no commas to separate each instance.
print formatter % (formatter, formatter, formatter, formatter)

# This line will print the four lines on one line.  Each retains the single quotes.
print formatter % ("I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight.")
# Note that the output of this line will have double quotes around the third string because there is a contraction
# within the string which uses the single quote.