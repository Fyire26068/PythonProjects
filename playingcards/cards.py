# Anthony Garrard
# 12/20
# cards Starting module
# import random


class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♥", "♦", "♣", "♠"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = str.format("""
        +----------+
        | {0:<2}{1}      |
        |          |
        |          |
        |          |
        |      {1}{0:>2} |
        +----------+
        """, self.rank, self.suit)
        return rep


class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        rep = ""
        if self.cards:
            for card in self.cards:
                rep += str(card)
        else:
            rep = "< EMPTY >"

        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, handsList, per_hand=1):
        for rounds in range(per_hand):
            for hand in handsList:
                if self.cards:
                    topcard = self.cards[0]
                    self.give(topcard, hand)
                else:
                    print("out of cards")
                    for hand in handsList:
                        hand.clear()
                    self.clear()
                    self.populate()
                    self.shuffle()
                    self.deal(handsList, per_hand)

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))


class PosCard(Card):
    def __init__(self, rank, suit):
        super(PosCard,self).__init__(rank, suit)
        self.faceup = True

    def flip(self):
        self.faceup = not self.faceup

    def __str__(self):
        if self.faceup:
            # super(PosCard, self).__str__()
            rep = str.format("""
                    +----------+
                    | {0:<2}{1}      |
                    |          |
                    |          |
                    |          |
                    |      {1}{0:>2} |
                    +----------+
                    """, self.rank, self.suit)
        else:
            rep = """
                    +----------+
                    |[][]][[][]|
                    |[]][##][[]|
                    |[][####][]|
                    |[]][##][[]|
                    |[][]][[][]|
                    +----------+
                    """
        return rep



mycard = PosCard(rank = 3, suit = "♥")
print(mycard)
mycard.flip()
print(mycard)

