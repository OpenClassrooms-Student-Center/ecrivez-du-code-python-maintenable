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


# On a créé un Deck
# Encore une classe qui hérite directement de la liste,
# dans l'initialisation nous ajoutons les différents types de cartes à notre
# deck, puis nous mélangeons le deck.
# Ajout shuffle (on refactorisera init pour appeler la méthode)
# drax_card ne fait rien que la liste ne puisse pas faire de base,
# mais la méthode possède un nom plus explicite que "pop".
# c'est une forme d'autodocumentation.
