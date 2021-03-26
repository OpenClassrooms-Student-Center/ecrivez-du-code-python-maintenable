"""Les cartes."""

import random
from typing import List


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


# new


class Controller:
    def __init__(self, deck: Deck):
        # models
        self.players: List[Player] = []
        self.deck = deck

        # views
        self.view = None

    def get_players(self):
        while len(self.players) < 5:  # nombre magique
            name = self.view.prompt_for_player()
            if not name:
                return
            player = Player(name)
            self.players.append(player)

    def start_game(self):
        self.deck.shuffle()
        for player in self.players:
            card = self.deck.draw_card()
            if card:
                player.hand.append(card)

    def run(self):
        self.get_players()

        self.start_game()
        for player in self.players:
            self.view.show_player_hand(player.name, player.hand)


# Créer le controller
# model + vue (deck passé en paramètre)
# méthode run qui est la principale
# intiialiser les joueurs
# ici on a pas encore notre vue mais on écrit les méthodes qu'on aimerait obtenir
# de la vue. On part d'un résultat souhaité pour ensuite l'implémenter
