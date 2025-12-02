# # Rock-Paper-Scissors Game


import random

while True:
    Choice = ["rock", "paper", "scissors"]
    print("=========================================================")
    usr_choice = input("Enter from rock 👊, paper 🖐️, scissors ✂️ :- ").lower()
    print("=========================================================")
    com_choice = random.choice(Choice)

    print(f"Computer chose: {com_choice}")

    if usr_choice not in Choice:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    if usr_choice == "rock" and com_choice == "paper":
        print("You Lose! Paper wraps Rock")
    elif usr_choice == "rock" and com_choice == "scissors":
        print("You Win! Rock crushes Scissors")
    elif usr_choice == "paper" and com_choice == "rock":
        print("You Win! Paper covers Rock")
    elif usr_choice == "paper" and com_choice == "scissors":
        print("You Lose! Scissors cut Paper")
    elif usr_choice == "scissors" and com_choice == "paper":
        print("You Win! Scissors cut Paper")
    elif usr_choice == "scissors" and com_choice == "rock":
        print("You Lose! Rock crushes Scissors")
    elif usr_choice == com_choice:
        print(f"Draw! Both chose {usr_choice}")
