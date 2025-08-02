import random
import sys
from typing import Optional

from src.mosh_hamedani.python_projects_for_beginners.dice_the_role.models import DiceModel
from src.mosh_hamedani.python_projects_for_beginners.dice_the_role.services.dice import DiceService
from src.mosh_hamedani.python_projects_for_beginners.dice_the_role.services.interfaces import DiceInterface


class Dice:
    def __init__(self,
                 dice_service: Optional[DiceInterface]):
        self.dice_service = dice_service or DiceService()

    def do_dice(self):
        while True:
            answer : bool = self.dice_service.get_data_from_user()
            if answer is True:
               dice1 = DiceModel(number=random.randint(1, 6))
               dice2 = DiceModel(number=random.randint(1, 6))
               print(dice1, dice2)
            else:
                print(f"Tanks for playing... ")
                break

if __name__ == "__main__":
    dice_object = Dice(dice_service=DiceService())
    dice_object.do_dice()