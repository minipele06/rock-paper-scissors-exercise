# game.py
import random

print("---------------")
print("Welcome to my Rock-Paper-Scissors game...")
print("---------------")

comp = ["Rock", "Paper", "Scissors"]

userchoice = input("Please Select Rock, Paper, or Scissors: ").title()

if userchoice != "Rock" and userchoice != "Paper" and userchoice != "Scissors":
    print("Invalid Response")
    exit()

compchoice = random.choice(comp)

if compchoice == "Rock" and userchoice == "Scissors":
    winner = "Oh, the computer won. It's ok."
elif compchoice == "Paper" and userchoice == "Rock":
    winner = "Oh, the computer won. It's ok."
elif compchoice == "Scissors" and userchoice == "Paper":
    winner = "Oh, the computer won. It's ok."
elif userchoice == "Rock" and compchoice == "Scissors":
    winner = "You Won!"
elif userchoice == "Paper" and compchoice == "Rock":
    winner = "You Won!"
elif userchoice == "Scissors" and compchoice == "Paper":
    winner = "You Won!"
else:
    winner = "It's a Draw."

print(f"You Chose: {userchoice}")
print(f"The Computer Chose: {compchoice}")
print("---------------")
print(winner)
print("---------------")
print("Thanks for playing. Please play again!")