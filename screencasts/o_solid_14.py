# solution possible ? Créer une classe qui possède la méthode d'évaluation.


class CheckerRankAndSuitIndex:
    def check(self, card, other):
        """Evalue la meilleur carte."""
        # code.


class Controller:
    def __init__(self, deck, view, checker_strategy):
        self.score_checker = checker_strategy()

    def evaluate(self, players):
        self.score_checker.check(players)


# lancer le code ensuite.
