import collections
from random import choice
Card = collections.namedtuple('Card', ['suit', 'rank'])

class FrenchDesk:
    ranks = [str (n) for n in range(2, 11)] + list('JQKA')
    # print(ranks)
    suits = "spades diamonds clubs hearts".split()
    # print(suits)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# _card_object = Card("7","diamond")
# print(_card_object)
desk = FrenchDesk()
# print(len(desk))

# print(desk[-2])
# print(desk[-1])
# print(desk[0])
# print(desk[1])

# for i in range(10):
#     print(choice(desk))

# print(desk[1:4:2])
# print(desk[::])

# for card in reversed(desk):
    # print(card)

# print(Card("7","beats") in desk)
# print(Card("Q","hearts") in desk)

