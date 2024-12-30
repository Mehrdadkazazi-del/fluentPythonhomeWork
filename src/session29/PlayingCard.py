from src.session29.__len__and__getitem__ import Card

class PlayingCard:
    def __init__(self):
        ranks = ['A', '2','3','4','5','6','7','8','9','10','J','Q','K','A']
        suits = ['clubs','hearts','diamonds','spades']

        #use list comprehension
        self.cards = [Card(rank,suit) for rank in ranks for suit in suits]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self,index):
        return self.cards[index]


playing_card = PlayingCard()
print(playing_card.cards[0])
print(len(playing_card))
print(playing_card[1:4])

for card in playing_card:
    print(card)