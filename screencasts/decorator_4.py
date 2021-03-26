from sub_decorator_4 import (
    get_on_the_ship,
    take_off_ship,
    land_ship,
    exit_the_ship,
    open_the_hold,
)


# def travel_from_to_earth_to_ganymede():
#     """Commence l'aventure, de la terre à Ganymède."""
#     get_on_the_ship()
#     take_off_ship()

#     print(travel_from_to_earth_to_ganymede.__doc__)

#     land_ship()
#     exit_the_ship()
#     open_the_hold()


# def travel_from_ganymede_to_kepler():
#     """Voyage de Ganymède à Kepler 438 b..."""
#     get_on_the_ship()
#     take_off_ship()

#     print(travel_from_ganymede_to_kepler.__doc__)

#     land_ship()
#     exit_the_ship()
#     open_the_hold()


# def travel_from_kepler_to_trappist():
#     """Voyage de Kepler 438 b à Trappist 1 d..."""
#     get_on_the_ship()
#     take_off_ship()

#     print(travel_from_kepler_to_trappist.__doc__)

#     land_ship()
#     exit_the_ship()
#     open_the_hold()


# travel_from_to_earth_to_ganymede()
# print()
# travel_from_ganymede_to_kepler()
# print()
# travel_from_kepler_to_trappist()


# ici on voit bien que notre code se répète souvent
# c'est embêtant pour des évolutions futures.


# def prepare_take_off_and_landing(function):
#     """Génère un décorateur qui s'occupe d'automatiser le décollage et l'atterissage."""

#     def wrapper(*args, **kwargs):
#         """Décore une fonction en ajoutant du code avant et/ou après."""
#         get_on_the_ship()
#         take_off_ship()

#         result = function(*args, **kwargs)

#         land_ship()
#         exit_the_ship()
#         open_the_hold()

#         return result

#     return wrapper


# ensuite on modifie nos fonctions :


# def travel_from_to_earth_to_ganymede():
#     """Commence l'aventure, de la terre à Ganymède."""
#     print(travel_from_to_earth_to_ganymede.__doc__)


# def travel_from_ganymede_to_kepler():
#     """Voyage de Ganymède à Kepler 438 b..."""
#     print(travel_from_ganymede_to_kepler.__doc__)


# def travel_from_kepler_to_trappist():
#     """Voyage de Kepler 438 b à Trappist 1 d..."""
#     print(travel_from_kepler_to_trappist.__doc__)


# enfin on les redéfinies

# travel_from_to_earth_to_ganymede = prepare_take_off_and_landing(
#     travel_from_to_earth_to_ganymede
# )


# # mais petit problème :
# travel_from_to_earth_to_ganymede()

# on perd malgré tout la documentation ! en effet, ce n'est plus la même fonction. :/


def prepare_take_off_and_landing(function):
    """Génère un décorateur qui s'occupe d'automatiser le décollage et l'atterissage."""

    def wrapper(*args, **kwargs):
        """Décore une fonction en ajoutant du code avant et/ou après."""
        get_on_the_ship()
        take_off_ship()

        result = function(*args, **kwargs)

        land_ship()
        exit_the_ship()
        open_the_hold()

        return result

    wrapper.__doc__ = function.__doc__  # ici !
    return wrapper


def travel_from_to_earth_to_ganymede():
    """Commence l'aventure, de la terre à Ganymède."""
    print(travel_from_to_earth_to_ganymede.__doc__)


travel_from_to_earth_to_ganymede = prepare_take_off_and_landing(
    travel_from_to_earth_to_ganymede
)

print()
travel_from_to_earth_to_ganymede()


# et voila le travail !
