"""Il s'agit ici d'utiliser la syntaxe pythonique des décorateurs."""

from sub_decorator_4 import (
    get_on_the_ship,
    take_off_ship,
    land_ship,
    exit_the_ship,
    open_the_hold,
)


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

#     wrapper.__doc__ = function.__doc__  # ici !
#     return wrapper


# def travel_from_to_earth_to_ganymede():
#     """Commence l'aventure, de la terre à Ganymède."""
#     print(travel_from_to_earth_to_ganymede.__doc__)


# travel_from_to_earth_to_ganymede = prepare_take_off_and_landing(
#     travel_from_to_earth_to_ganymede
# )

# print()
# travel_from_to_earth_to_ganymede()


# comment changer notre code pour le faire correspondre à cette nouvelle syntaxe ?


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


@prepare_take_off_and_landing
def travel_from_to_earth_to_ganymede():
    """Commence l'aventure, de la terre à Ganymède."""
    print(travel_from_to_earth_to_ganymede.__doc__)


print()
travel_from_to_earth_to_ganymede()


# A l'execution, python va décorer la fonction, ça revient exactement au même.
