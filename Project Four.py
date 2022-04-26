'''
Objective:  to make a Rock, Paper, Scissors game for the user 
to play against the computer

@author: Grace Nguyen
'''
while():
     print("Welcome to Rock Paper Scissors! BEst two out of three. Press 'q' to quit")
    c = 0
    y = 0
    
    question1 = print("Rock, paper, scissors, or q?")


choice = input("Answer: ")
    
    def itemChoice(r, p, s):
    r = "rock"
    p = "paper"
    s = "scissors"
    
    print(itemChoice(r, p, s))
    
    if itemChoice == choice:
        print(DRAW)
        print("User:" y", Computer:" c)
        
    if itemChoice == r and choice == "paper":
        y = y + 1
        print("User:" y", Computer:" c)
    
    if itemChoice == p and choice == "scissors":
        y = y + 1
        print("User:" y", Computer:" c)
        
    if itemChoice == s and choice == "rock":
        y = y + 1
        print("User:" y", Computer:" c)
        
    if itemChoice == p and choice == "rock":
        c = c + 1
        print("User:" y", Computer:" c)
        
    if itemChoice == r and choice == "scissors":
        c = c + 1
        print("User:" y", Computer:" c)
        
    if itemChoice == s and choice == "paper":
        c = c + 1
        print("User:" y", Computer:" c)
        
    if choice == "q":
        quit
        
    if choice != "rock", "paper", "scissors", or "q":
        print("Not an option try again.")
    
    if c == 2:
        print("Thanks for playing!")
        print(c)
        print(y)
        print("CPU wins!")
        
    if p == 2:
        print("Thanks for playing!")
        print(y)
        print(c)
        print("You win!")
        
        
        