'''
Objective:
The Objective of this program is to quiz the user on basic high school
trivia. The tasks to complete are:
Ask the user each of the following questions:
    1) What is the powerhouse of the cell?
        A) mitochondria B) nucleus C) ribosome
    2) How many states comprise the United States?
        A) 13 B) 45 C) 50
    3) In y = mx + b, what does m stand for?
        A) slope B) output C) I don't understand math
    4) In English, a person, place or thing is called:
        A) verb B) adjective C) noun
The user should input a letter for each question. (A, B, or C)
Check the users answer, if it is correct print "Correct", else it should print "Incorrect, the correct answer is [insert]"
Additionally, the program should track how many questions the user got correct and at the end give them a score out of 4. And give them a percentage.

@author:Grace Nguyen
'''

score = 0

question1 = print("1) What is the powerhouse of the cell? a) mitochondria b) nucleus c) ribosome")

ans1 = "a"

ans = input("Answer: ")

if(ans == ans1):
    print("Correct")
    score = score + 1
    
else:
    print("Incorrect, the correct answer is A.")
    
question2 = print("2) How many states comprise the United States? a) 13 b) 45 c) 50")

ans2 = "c"

ans = input("Answer: ")

if(ans == ans2):
    print("Correct")
    score = score + 1
    
else:
    print("Incorrect, the correct answer is C.")

question3 = print("3) In y = mx + b, what does m stand for? a) slope b) output c) I don't understand math")

ans3 = "a"

ans = input("Answer: ")

if(ans == ans3):
    print("Correct")
    score = score + 1
    
else:
    print("Incorrect, the correct answer is A.")

question4 = print(" 4) In English, a person, place or thing is called: a) verb b) adjective c) noun")

ans4 = "c"

ans = input("Answer: ")

if(ans == ans4):
    print("Correct")
    score = score + 1
    
else:
    print("Incorrect, the correct answer is C.")
    
p = score/4

print("You got a " + str(score) + "/4 or in other words a " + str(p*100) + "%")

