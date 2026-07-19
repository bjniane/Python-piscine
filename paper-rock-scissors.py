import random

choices = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in choices:
        continue

    computer_guess = random.choice(choices)
    print("Computer picked:", computer_guess)

    if user_input == "rock" and computer_guess == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_guess == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_guess == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")