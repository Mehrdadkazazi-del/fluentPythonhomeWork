import random


class NumberGuessingGame:
    @classmethod
    def guess(cls):
        target_number = cls._generate_random_number()
        while True:
            try:
                prediction_number = int(input("Guess the number between 1 and 100:"))
                if target_number < prediction_number:
                    print("too high !")
                if target_number > prediction_number:
                    print("too low !")
                else:
                    print("you guessed right!")
                    break
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 100.")

    @classmethod
    def _generate_random_number(cls):
        return random.randint(1, 100)


if __name__ == '__main__':
    NumberGuessingGame.guess()
