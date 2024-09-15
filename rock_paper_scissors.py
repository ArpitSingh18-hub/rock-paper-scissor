import random

print("Welcome to the game of rock , paper,scissors ")
action_allowed=["rock","paper","scissors"]
user_action=input("Choose rock,paper,scissors\n")
computer_action=random.choice(action_allowed)
print(f" Your action --> {user_action}.\n Computer action --> {computer_action}." )
if user_action == computer_action:
    print(f" Both selected the same {user_action} Game is tied play again ")
elif user_action =="rock":
    if computer_action =="scissors":
     # print(f"user action ==" ,user_action)
     # print(f"computer action ==" ,computer_action)
     print("Rock smashed the scissors")
     print("You Won !")
    else:
     print("Paper cover the Rock ! YOU LOOSE ")

elif user_action == "paper" :
    if computer_action == "rock":
     # print(f"user action ==", user_action)
     # print(f"computer action ==", computer_action)
     print("Paper cover the rock")
     print("You Won !")
    else:
       print("Scissors makes the pieces of the paper! YOU LOOSE ")




elif user_action == "scissors":
    if computer_action == "paper":
     # print(f"user action ==", user_action)
     # print(f"computer action ==", computer_action)
     print("Scissors makes the pieces of the paper")
     print("You Won !")
    else:
      print("Rock Smashed the scissors ! YOU LOOSE ")


# play_again = input("Do you want to play again Y/N ")
# if play_again.lower() !="Y":
#  break: