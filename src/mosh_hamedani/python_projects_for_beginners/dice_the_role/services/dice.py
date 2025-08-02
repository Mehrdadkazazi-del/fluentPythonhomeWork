import re

from src.mosh_hamedani.python_projects_for_beginners.dice_the_role.services.interfaces import DiceInterface


class DiceService(DiceInterface):

    def get_data_from_user(self):
        input_answer = input(f"Roll the dice?")
        if re.fullmatch(r"[yn]", input_answer, re.IGNORECASE):
            return input_answer.lower() == "y"
        print("Invalid input! Please enter 'y' or 'n'.")