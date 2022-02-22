2qa'''

I will make a program that can have the user input a number of 
miles and print out the distance converted to yards, feet, 
and inches.

@author: Grace
'''
#Use input() to get the number of miles from the user. And store
#that int in a variable called miles.

miles = int(input("How many miles would you like to convert?"))

#Convert miles to yards, using the following:
# 1 mile = 1760 yards.
#
#Store the value in a variable called yards and print it out with a 
#simple statement.

yards = miles * 1760 
print("Your number of yards:" + str(yards))

#Convert miles to feet, using the following:
# 1 mile = 5280 feet.
#
#Store the value in a variable called feet and print it out with a 
#simple statement.

feet = miles * 5280
print("Your number of feet:" + str(feet))

#Convert miles to inches, using the following:
# 1 mile = 63,360 inches.
#
#Store the value in a variable called inches and print it out with a 
#simple statement.

inches = miles * 63360
print("Your number of inches:" + str(inches))
