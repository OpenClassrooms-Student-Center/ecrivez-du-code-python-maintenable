"""Les cartes."""

import random


SUITS = ("trèfles", "coeurs", "piques", "carreaux")
RANKS = (
    "deux",
    "trois",
    "quatre",
    "cinq",
    "six",
    "sept",
    "huit",
    "neuf",
    "dix",
    "valet",
    "reine",
    "roi",
    "ace",
)


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.is_face_up = False

        self._rank_score = RANKS.index(self.rank)
        self._suit_score = SUITS.index(self.suit)

    def __str__(self):
        return f"{self.rank} de {self.suit}"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other: "Card"):
        if self._rank_score != other._rank_score:
            return self._rank_score < other._rank_score

        return self._suit_score < other._suit_score


card1 = Card("trèfles", "cinq")
card2 = Card("coeurs", "cinq")
card3 = Card("coeurs", "valet")
print(card1 < card2)
print(card3 > card2)


class Deck(list):
    def __init__(self):
        for rank in RANKS:
            for suit in SUITS:
                card = Card(suit, rank)
                self.append(card)
        random.shuffle(self)

    def shuffle(self):
        random.shuffle(self)

    def draw_card(self):
        try:
            return self.pop()
        except IndexError:
            return None


deck = Deck()
print(deck)

# Du nouveau ici


class Hand(list):
    def append(self, object):
        if not isinstance(object, Card):
            return ValueError("Vous ne pouvez ajouter que des cartes !")
        return super().append(object)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()


# La classe Hand implémente la liste, c'est donc une liste !

# on modifie légèrement la méthode append pour s'assurer qu'on n'ajoute que
# des cartes. C'est une liste moins permissive. Elle n'est pas totalement
# sécurisée puisqu'on peut encore ajouter des objets par des moyens détournés,
# comme lors de l'initialisation ou via la méthode extends. Mais c'est déjà pas
# mal.

# la classe player est très simple puisqu'elle ne prendre qu'un nom, et une "main".
