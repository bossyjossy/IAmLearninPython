# This is my completed exercise for Learn Python The Hard Way Exercise 4
#
# This is slightly modified from the lesson so that I can test things out
# and really solidify what I learned.
#
# EXERCISE 4: Variable and Names

# -------------------------------------------------------------------------
# Setting the variables
# -------------------------------------------------------------------------
# There are 100 cars.
cars = 100
# There is space in each car for 4 people.
space_in_a_car = 4.0
# There are 30 drivers.
drivers = 30
# There are 90 passengers.
passengers = 90
# How many cars cannot be driven?  (i.e. not enough drivers)
cars_not_driven = cars - drivers
# How many cars can be driven?  This is equal to the number of drivers.
cars_driven = drivers
# Maximum carpool capacity of a car?
carpool_capacity = cars_driven * space_in_a_car
# What is the average number of passengers per car? 
average_passengers_per_car = passengers / cars_not_driven

# -------------------------------------------------------------------------
# Summary of the data
# -------------------------------------------------------------------------
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "cars sitting at home undriven today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "available to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
