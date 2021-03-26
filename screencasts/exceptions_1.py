def get_number():
    """Get a number input and return it's value."""
    return int(input("Sélectionnez un nombre: "))


number = get_number()
print("Le nombre est", number)

# problème: si on met autre chose qu'un nombre entier ça plante


def get_number():
    """Get a number input and return it's value."""
    try:
        choice = input("Sélectionnez un nombre: ")
        number = int(choice)
        return number
    except:
        print(f"{choice} n'est pas un nombre ! On retourne None.")
        return None


number = get_number()
print("Le nombre est", number)


# problème: KeyboardInterrupt ou autres erreurs bypassées.
# même version en ajoutant Exception


def get_number():
    """Get a number input and return it's value."""
    try:
        choice = input("Sélectionnez un nombre: ")
        number = int(choice)
        return number
    except ValueError:
        print(f"{choice} n'est pas un nombre ! On retourne None.")
        return None


number = get_number()
print("Le nombre est", number)

# ici on sait ce qu'on récupère !
# Astuce pour savoir quelle erreur récupérer : utiliser l'interpréteur Python
# et essayer de la générer


def get_number():
    """Get a number input and return it's value."""
    try:
        choice = input("Sélectionnez un nombre: ")
        number = int(choice)
        return number
    except ValueError:
        raise ValueError(f"{choice} n'est pas un nombre !")


number = get_number()
print("Le nombre est", number)

# Autre possibilité : générer l'erreur avec un message perso.
# Mieux vaut un programme qui plante bien qu'un programme qui tourne mal !


def get_number():
    """Get a number input and return it's value."""
    try:
        choice = input("Sélectionnez un nombre: ")
        number = int(choice)
        return number
    except ValueError as error:
        print(error)


number = get_number()
print("Le nombre est", number)


# il est possible de récupérer un objet Exception pour afficher son message par exemple.
