# This is my completed exercise for Learn Python The Hard Way Exercise 3
#
# This is slightly modified from the lesson so that I can test things out
# and really solidify what I learned.
#
# EXERCISE 3: Numbers and Math

print "I will now count my chickens."

# This next line will show that I can print a string and then do some math.  Remember order of operations.
print "Hens:", 25 + 30 / 6

# This next line includes the operation called "modulo"
# The modulo operation finds the remainder after division of one number by another.
# In Order of Operations, modulo is at the same level as multiplication and division.
print "Roosters:", 100 - 25 * 3 % 4
# Solution: 25*3=75.  Then 75%4 means 'remainder of 75/4' which is 3.  Therefore the answer is 100-3=97

# This next math example will start to illustrate floating point arithmetic as opposed to decimal math.
# Floating point arithmetic is used in computing systems. 
print "Now I will count the eggs:"
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# Solution: The answer should be 6.75, but since whole numbers are being used, it is rounded up. Alternatively,
# if I printed the answer to 1/4, it would be 0 as it would round down.

# In this next example, we will see that python will evaluate the expression.
print "Is it true that 3 + 2 < 5 - 7?"
print 3 + 2 < 5 - 7
# Solution: 5 is not less than -2 so it will print False.
print "What is 3+2? ", 3 + 2
print "What is 5-7? ", 5 - 7

print "Oh, that's why it is False!"

# More inequalities to be evaluated
print 
print "Is it instead greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less than or equal", 5 <= -2

# Now, I'm going to use fractions so that I can test out the floating point arithmetic further.
# Using one number as a non-whole number changes the answer to use decimal points.
print "Hens:", 25.0 + 30 / 6
# Solution: No real change
print "Roosters:", 100.0 - 25 * 3 % 4
# Solution: No real change
print "Now I will count the eggs:"
# If I make the first number a decimal, we will see that the equation is still evaluated the same way
# but the answer will be a decimal number instead of a whole number
print "Eggs with first number of equation a decimal:"
print 3.0 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# However, if I make the fraction the decimal number, the final answer is different!!!!
print "Eggs with the fraction as a decimal:"
print 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4 + 6




