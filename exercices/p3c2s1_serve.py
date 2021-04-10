"""Sert un groupe de clients."""


GUESTS_NUMBER = 15
WATER_PER_GUEST = 400
WATER_LEVEL = GUESTS_NUMBER * WATER_PER_GUEST

SPOONS_PER_GUEST = 2
MUSIC_VOLUME = 2
TIME_TO_WAIT = 2


def serve_group_of_two():
    """Sert un groupe de deux clients affamés.

    S'assure d'une expérience inoubliable !
    """
    greet_guests()
    table_number = prepare_table(GUESTS_NUMBER)
    for guest in range(GUESTS_NUMBER):
        lay_spoons_on_table(SPOONS_PER_GUEST)

    lead_customers_to_table(table_number)
    fill_water_carafe(WATER_LEVEL)
    adjust_music_volume(MUSIC_VOLUME)
    present_menus(GUESTS_NUMBER)

    wait_minutes(TIME_TO_WAIT)

    drinks_order = take_order(table_number)
    process_order(drinks_order)
    # ...


# On met les autres méthodes ici


def greet_guests():
    print("Bienvenue !")


def prepare_table(guests):
    print(f"Nous servons une table pour {guests}")
    return 10


def lay_spoons_on_table(spoons):
    print(f"Nous servons {spoons} cuillères.")


def lead_customers_to_table(table_number):
    print(f"Venez à la table {table_number} !")


def fill_water_carafe(water_level):
    print(f"Nous vous servons {water_level} ml d'eau.")


def adjust_music_volume(level):
    print(f"Nous mettons le volume à {level}.")


def present_menus(number):
    print(f"Nous présentons {number} menus.")


def wait_minutes(minutes):
    print(f"--- attente de {minutes} minutes ---")


def take_order(number):
    print(f"Nous prenons la commande de la table {number}.")
    return "Bouteille de vin"


def process_order(drinks_order):
    print("Nous allons chercher les boissons !")


if __name__ == "__main__":
    serve_group_of_two()
