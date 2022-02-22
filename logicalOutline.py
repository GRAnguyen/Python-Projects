'''
This outline will help solidify concepts from the Logical Operators lesson.
Fill in this outline as the instructor goes through the lesson.
'''
#EX) Make two boolean variables. Put them on either side of the and operator.
#Store this expression in a variable named a. Print the variable.
from builtins import True, False
one = True
two = False
a = one and two 
print(a)

#1) Make two boolean variables. Put them on either side of the and operator.
#Store this expression in a variable named a. Print the variable.

three = True
four = False

a = three or four
print(a)

#2) Make two boolean variables. Put them on either side of the or operator.
#Store this expression in a variable named b. Print the variable.

five = True
six = True

b = five and six
print(b)

#3) Make one boolean variable. Put the variable after the not. Store this 
#expression in a variable named c. Print the variable.

c = not 5 == 3
print(c)

#4) Make a logical expression with one of the common SYNTAX errors.

seven = False
nine = False

d = not seven == nine
print(d)
