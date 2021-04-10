"""Il s'agit ici d'utiliser la syntaxe pythonique des décorateurs."""

# ---------------------
# --- Le décorateur ---


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

    # on donne la docstring de 'function' à 'wrapper' !
    wrapper.__doc__ = function.__doc__

    return wrapper


# --------------------------------
# --- nos fonctions de voyages ---


@prepare_take_off_and_landing
def travel_from_to_earth_to_ganymede():
    """Commence l'aventure, de la terre à Ganymède."""
    print(travel_from_to_earth_to_ganymede.__doc__)


@prepare_take_off_and_landing
def travel_from_ganymede_to_kepler():
    """Voyage de Ganymède à Kepler 438 b..."""
    print(travel_from_ganymede_to_kepler.__doc__)


@prepare_take_off_and_landing
def travel_from_kepler_to_trappist():
    """Voyage de Kepler 438 b à Trappist 1 d..."""
    print(travel_from_kepler_to_trappist.__doc__)


# ---------------------------------
# --- Nos fonctions utilitaires ---


def get_on_the_ship():
    print("Les astronautes montent dans le vaisseau")


def take_off_ship():
    print("Le vaisseau décolle !")


def land_ship():
    print("Le vaisseau atterit.")


def exit_the_ship():
    print("Les astronautes sortent du vaisseau")


def open_the_hold():
    print("Ils ouvrent la soute pour sortir le matériel d'expedition.")


# -------------------------
# --- Lancement du code ---


if __name__ == "__main__":
    print()
    travel_from_to_earth_to_ganymede()
    print()
    travel_from_ganymede_to_kepler()
    print()
    travel_from_kepler_to_trappist()
