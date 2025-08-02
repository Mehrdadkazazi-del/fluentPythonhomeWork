import re
import random


class RockPaperScissors:

    @classmethod
    def play_game(cls):
        emojis = {"r": "rock", "p": "paper", "s": "scissor"}
        computer_choice = random.choice(["r", "p", "s"])
        while True:
            decision = input("Rock , Paper or Scissors? (r/p/s)").lower()

            if not re.match(r'^[rps]$', decision):
                print("Invalid input! Please enter 'r', 'p', or 's'.")
                continue
            print(f"you chose {emojis[decision]}")
            print(f"computer chose {emojis[computer_choice]}")

            outcomes = {
                "r": {"r": "equal", "p": "loos", "s": "win"},
                "p": {"r": "win", "p": "equal", "s": "loos"},
                "s": {"r": "loos", "p": "win", "s": "equal"}
            }

            result = outcomes[decision].get(computer_choice, "Invalid outcome")
            if result == "equal":
                print("It's a tie!")
            elif result == "win":
                print("You win!")
            elif result == "loos":
                print("You lose!")

            continue_command = input("continue? (y/n)")
            if continue_command == "n":
                break
            else:
                continue


if __name__ == "__main__":
    RockPaperScissors.play_game()