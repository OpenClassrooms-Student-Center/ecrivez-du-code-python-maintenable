from controller_10 import Controller
from controller_9 import Deck
from view_11 import View


def main():
    deck = Deck()
    view = View()
    game = Controller(deck, view)
    game.run()


main()

# très simple, il suffit d'appeler la méthod erun de notre controller.
# demo console.
