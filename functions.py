#Stuff to do: Add a sleep between each print statement so paragraphs don't just pop up in the user's face. Fix the problem of game crash is user doesn't input 1 or 2. Fix any typos

import time
#Chris
def greeting():
    name = str(input("Greetings user! What is your name? Name: "))
    print("Ok, " + str(name) + ", let's play a game. in a few seconds I am going to put you through a series of decisions and it is up to you to make it out alive.")
    ready()

def ready():
    start = input("Are you ready? (Yes/No) : ")
    if (start == "Yes"):
        print("Great! The game will start in 3")
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print(0)
        print("---------------------------------------------------------------------------------------------------")
        intro()
    if (start == "yes"):
        print("Great! The game will start in 3")
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print(0)
        time.sleep(1)
        print("---------------------------------------------------------------------------------------------------")
        intro()
    if (start == "No"):
        print("Since you are not ready,  the game will now close.")
        exit()
    if (start == "no"):
        print("Since you are not ready,  the game will now close.")
        exit()
        
def intro():
    print("You are a tourist and you have gotten lost. You were walking on a trail but lost it.")
    print("While wandering, you come across a cave and a trail, but it doesn't look like the trail from earlier.")
    ichoice = int(input("Do you go into the cave? Or do you take the trail? (Type '1' for the cave or '2' for the trail) : "))
    if (ichoice == 1):
        print("---------------------------------------------------------------------------------------------------")
        cave()
    if (ichoice == 2):
        print("---------------------------------------------------------------------------------------------------")
        trail()
    
def cave():
    print("You have entered the cave.")
    print("It is a long, dark tunnel. You come across a point where the cave splits into two.")
    cave_choice = int(input("Do you go left? Or right? (Type '1' for left or '2' for right) : "))
    if (cave_choice == 1):
        print("---------------------------------------------------------------------------------------------------")
        pond()
    if (cave_choice == 2):
        print("---------------------------------------------------------------------------------------------------")
        clown()

def pond(): #This is left after cave
    print("You walk along the long path, wondering if your choice was right.")
    print("You begin to worry as there doesn't seem to be anything.")
    print("Finally the cave opens up to a giant pond. There seems to be a small tunnel in the pond but it is underwater.")
    print("There is also a broken path leading up to the top of the cave. It looks like it could collapse at any moment.")
    print("Do you swim into the underwater tunnel or take the risky path to the top of the cave? ")
    pond_choice = int(input("Type '1' for water tunnel or '2' for the path : "))
    if (pond_choice == 1):
        print("---------------------------------------------------------------------------------------------------")
        watertunnel()
    if (pond_choice == 2):
        print("---------------------------------------------------------------------------------------------------")
        pond_path()
    
    
def watertunnel():
    print ("You walk along the water tunnel and it gradually gets deep")
    print ("Suddenly, THERES A WHIRLPOOL!!!")
    print ("You struggle for air but it was no help. You drown.")
    print ("YOU LOSE.")
    restart()

def clown(): # this is right after the cave
    print ('Unexpectedly, A CLOWN POPPED UP FROM NOWHERE!!!')
    print ('The clown asks "do you want a balloon?"')
    clown_choice = int(input("Do you want to take the balloon? (Type '1' to take it or '2' to leave it) : "))
    if (clown_choice == 1):
        print("---------------------------------------------------------------------------------------------------")
        win()
    if (clown_choice ==2):
        print("---------------------------------------------------------------------------------------------------")
        lose()

def pond_path():
    print("There is a path that appears to be going up.")
    print("You walk up and find GOLD and an exit.")
    print("You WIN!")
    restart()
    
    
def win():
    print("You have now made the risky choice of taking the balloon AND it was the RIGHT one.")
    print ("The balloon flies you up to gold and YOU WIN")
    restart()
    
def lose(): 
    print ("The clown eats you, the balloon was the escape.")
    print ("You LOSE.")
    restart()

def trail():
    print ("You have are now walking on the trail!")
    print ("HOWEVER now the trial forks left and right!")
    trail_choice = int(input("Do you go left or right? (Type '1' for left or '2' for right ): "))
    if (trail_choice == 1):
        print("---------------------------------------------------------------------------------------------------")
        cave_in()
    if (trail_choice ==2):
        print("---------------------------------------------------------------------------------------------------")
        quicksand()
    
def cave_in():
    print("You have been walking on this trial for about an hour.")
    print("Suddenly, THE TRIAL CAVES IN")
    print(" You fall into a tunnel and decide to keep walking foward instead of looking back.")
    print("---------------------------------------------------------------------------------------------------")
    pond()

def quicksand(): 
    print ("You have now walked for an hour going right.")
    print("Suddenly, YOU WALK INTO QUICKSAND!!!")
    quicksand_choice = int(input("Do you want to try and escape or wait and do nothing? (type '1' for try to escape or '2' for waiting : "))
    if (quicksand_choice ==1):
        print("---------------------------------------------------------------------------------------------------")
        dies()
    if (quicksand_choice ==2):
        print("---------------------------------------------------------------------------------------------------")
        print ("You wait and sink through the quicksand. You now appear in a cave.")
        clown()
        
        
def dies():
    print("You have suffocated and died.")
    restart()
    
def restart():
    print("---------------------------------------------------------------------------------------------------")
    game_restart = input("The game has ended. Would you like to restart? (Yes/No) : ")
    if (game_restart == "Yes"):
        greeting()
    if (game_restart == "No"):
        quit()
    if (game_restart == "yes"):
        greeting()
    if (game_restart == "no"):
        quit()
