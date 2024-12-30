class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.__class__.__name__}(rank = {self.rank},suit = {self.suit})"




