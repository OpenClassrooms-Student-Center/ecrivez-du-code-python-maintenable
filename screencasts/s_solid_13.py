# l'évaluation doit être ailleurs. Dans le joueur ?
# mauvaise idée, car un joueur est sensé dfinir une personne
# dans sa forme la plus simple, et non un calcul de score

# La vue casse aussi le SRP car trop de méthodes différentes !

# le controller == gérer les séquences de l'application, mettre à jour le jeu
# donc on est bon.

# on va juste enelever la méthode __lt__ de la classe Card pour définir l'évaluation
# dans le controller.


class Controller:
    def evaluate_game(self):
    last_player = self.players[0]
    best_candidate = self.players[0]

    for player in self.players[1:]:
        player_card = player.hand[0]
        last_player_card = last_player.hand[0]

        player_rank = # méthode
        other_rank = # méthode
        if player_rank > other_rank:
            best_candidate = player

        last_player = player

    return best_candidate.name
