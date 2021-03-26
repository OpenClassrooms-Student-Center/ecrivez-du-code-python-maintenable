def get_number_input():
    try:
        choice = input("Tapez un nombre : ")
        return int(choice)
    except:
        print("Une erreur !")


number = get_number_input()
print("Le nombre tapé est", number)
