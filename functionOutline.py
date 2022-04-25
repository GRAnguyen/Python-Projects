'''
This outline will help solidify concepts from the Functions lesson.
Fill in this outline as the instructor goes through the lesson.
'''
from builtins import False

#1) Make a function that has two boolean parameters. If both booleans are
#true, return true. Else, return false. Then, call the function.
#Print what the function returns.

def questionOne(True, False):
    return False

y = False
print(questionOne(y))

#2) Make a function that takes one int parameter: gallons. Convert gallons
#to cups (do this by multiplying gallons by 16). Then return cups. Then,
#call the function.
#Print what the function returns.

def measurmentConversions(gallons):
    cups = gallons * 16
    return cups

x = 5
print(measurmentConversions(x))

#3) Make a function of any any kind with a common SYNTAX error. Then, call the
#function.
#Print what the function returns.

def lengthConversions(feet)
    inches = feet * 12
    return inches

z = 6.4
print(lengthConversions(z))
