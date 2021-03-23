"""Sert un groupe de clients."""


def serve_group_of_two():
    """Sert un groupe de deux clients affamés.

    S'assure d'une expérience inoubliable !
    """
    greet_guests()
    table_number = prepare_table(2)
    for guest in range(2):
        lay_spoons_on_table(2)

    lead_customers_to_table(table_number)
    fill_water_carafe(800)
    adjust_music_volume(2)
    present_menus(2)

    wait_minutes(2)

    drinks_order = take_order(table_number)
    process_order(drinks_order)
    # ...
    present_bill()
    thank_guests()


# problème de nombre qui se répète et qui n'est pas documenté

GUESTS_NUMBER = 15
SPOONS_PER_GUEST = 2
MUSIC_VOLUME = 2
TIME_TO_WAIT = 2
WATER_PER_GUEST = 400
WATER_LEVEL = GUESTS_NUMBER * WATER_PER_GUEST


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
    present_bill()
    thank_guests()


# En expliquant le code, on peut retrouver le nom de chaque constante.
# Plutot que de changer les variables une à une, on va changer nos constantes,
# qui font office de configuration du programme.
