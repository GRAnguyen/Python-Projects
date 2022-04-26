'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function.

EXAMPLE TASK:
'''
#EX) Define a function that has two parameters. Make the function add the two
#numbers together and return the result.
from builtins import True, False
from pip._internal.cli.progress_bars import BlueEmojiBar
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that has two int parameters. Make the function subtract 
#the first parameter minus the second one. Then, return the result. Now call 
#the function.
#Print what the function returns.

def subtract_two_numbers(num1, num2):
    differenceOfTwoNumbers = num1 - num2
    return differenceOfTwoNumbers

x = 2
y = 5
subtract_two_numbers(x,y)
num = subtract_two_numbers(x,y)
print(subtract_two_numbers(x,y))

#2) Define a function that has one parameter. Make the function divide the 
#parameter by 2, multiply it by 77, and then add 10,000. Return the result.
#Now call the function.
#Print what the function returns.

def mathFunction(num1):
    mathOfNumbers = num1/2*77*10000
    return mathOfNumbers
z = 23
print(mathFunction(x))

#3) Define a function that has two int parameters. Make the function check if 
#two numbers are equal. If they are equal, return true. If they are not equal, 
#return false. Now call the function.
#Print what the function returns.

def equivilentFunction(num1, num2):
    if num1 == num2:
        return True
    else:
        return False
    
a = 7
b = 2
print(equivilentFunction(a,b))

#4) Define a function that has two int parameters. Make the function
#check which parameter is bigger, and return the bigger parameter. 
#If they are the same, it should just return either parameter. Now call the 
#function.
#Print what the function returns.

def funFunction(num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return num1
    
c = 12
d = 3
print(funFunction(c,d))

#5) Define a function that has two string parameters. Make the function
#add the two strings together. And then return the combined string. Now call 
#the function.
#Print what the function returns.

def stringFunction( str1, str2):
    name = str1 + str2
    return name

e = "day"
f = "light"
print(stringFunction(e,f))

#6) Define a function that has three int parameters. If the first number is 
#equal to the second OR the third number, return true. Else, return false. Now 
#call the function.
#Print what the function returns.

def anotherFunction(num1, num2, num3):
    if num1 == num2:
        return True
    elif num1 == num3:
        return True
    else:
        return False

g = 4
h = 8
i = 4
print(anotherFunction(g,h,i))

#7) Define a function that prints your name. It should have no parameters and 
#shouldn't return anything. Now call the function.

def nameFunction(name):

name = "Grace

#8) Define a function that has one string parameter. The string should be a
#color. If that string is equal to your favorite color, it prints "That's my 
#favorite color!". If it is not, it prints "That is not my favorite color. 
#Try again.". It shouldn't return anything. Now call the function.

def stringFunction(colorStr):
    if colorStr = "pink":
        print("That's my favorite color!")
    else:
        print("That is not my favorite color. Try again.")
        
colorStr = "blue"

#9) Define a function that has one int parameter. The int should be 
#positive. If the number is not equal to zero, the function runs a loop that
#decrements the parameter by 1 and prints it each time. Now call the function.

def analyisisFunction(positiveNum):
    while( positiveNum > 0):
        print(positiveNum)
        positiveNum = positiveNum - 1
        
t = 25
analysisFunction(t)
        
    
