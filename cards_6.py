"""Les cartes."""

SUITS = ("diamonds", "coeurs", "piques", "carreaux")
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

    def __str__(self):
        return f"{self.rank} de {self.suit}"

    def __eq__(self, other):
        other_rank = RANKS.index(other.rank)
        our_rank = RANKS.index(self.rank)
        return our_rank == other_rank

    def __lt__(self, other):
        other_rank = RANKS.index(other.rank)
        our_rank = RANKS.index(self.rank)
        return our_rank < other_rank


card1 = Card("diamonds", "cinq")
card2 = Card("coeurs", "cinq")
card3 = Card("coeurs", "valet")
print(card1 == card2)
print(card1 < card2)
print(card3 > card2)


# On définit 2 constantes, les suites, et les scores.
# On définit ensuite une classe de Carte, qui doit avoir une suite, un score...
# et définir si elle est face recto ou verso.
# petite parenthèse pour les noms de booléens : les commencer par
# is ou has (pour "est quelque chose" ou "possède quelque chose").
# du coup on comprend directement qu'on a affaire à un booléen !

# pour la carte, on ajoute trois méthodes magiques :
# la méthode str qui permet de retourner une forme lisible de la carte
# et les méthode de comparaison pour l'égalité ou l'infériorité.
# ces méthodes permettent de faire des opérations entre les objets cartes,
# comme on le ferait avec des nombres
