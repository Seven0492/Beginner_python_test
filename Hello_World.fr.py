class bcolors:
    Green = '\033[92m'  # GREEN
    Yellow = '\033[93m'  # YELLOW
    Red = '\033[91m'  # RED
    LIGHT_BLUE = "\033[1;34m"  # Light Blue
    RESET = '\033[0m'  # RESET COLOR


def main():
    print("\"" + bcolors.Green + "Hallo Monde!" + bcolors.RESET + "\"\n")

    is_exit = input(bcolors.Yellow + "Ece que tu veux continuer tester ou terminer sa maintenant?"
                    + bcolors.LIGHT_BLUE + " (Vraie ou Faux): " + bcolors.RESET)
    print("\n")

    if is_exit.lower() == "faux":
        exit(1)

    pass


def checks():
    print(bcolors.Green + "Hallo Monde!" + bcolors.LIGHT_BLUE
          + " (pour la deuxième fois, tu as entrer dans un monde dans un autre monde)\n" + bcolors.RESET)

    name = input(bcolors.Yellow + "Pouvez-vous taper votre nom pour le programe?: " + bcolors.RESET)

    if name is None:
        print(bcolors.Yellow
              + "Tu dois taper quelque chose! Donc pour ta paresse tu devras recommencer le programe pour continuer!"
              + bcolors.RESET)
        return False

    y_or_n = str(input(bcolors.Yellow + "\nTon nom est " + bcolors.Green + name + bcolors.Yellow + ", correcte?"
                       + bcolors.LIGHT_BLUE + " (o or n): " + bcolors.RESET))

    if y_or_n.lower() == "o" or y_or_n.lower() == "oui":
        return True

    if y_or_n.lower() == "n" or y_or_n.lower() == "non":
        return False

    print(bcolors.Yellow + "Ce que tu as taper n'est pas 'o' ni 'n', mais '" + bcolors.Green + y_or_n
          + bcolors.Yellow + "', cette réponse n'est pas supporter...\n\n")
    return False

    pass


global menu_choices
# Ajoute le nombre des options qu'and tu en rajoutes ici, ou sa va buggés
menu_choices = [1]


def calculator_menu():
    print(bcolors.Yellow
          + "Sens toi chanceux(se), tu peux choisir entre 1 type de calcul avec deux nombres, fais ton choix")

    print(bcolors.LIGHT_BLUE + "1." + bcolors.Yellow + " Addition" + bcolors.RESET)

    calculator_choice()
    pass


def calculator_choice():
    choice = input(bcolors.Yellow + "Fais ton choix (ex: 1 or 2): " + bcolors.RESET)

    print("\n")

    choice_location = int(choice) - 1

    if int(choice) == menu_choices[choice_location]:
        if choice_location == 0:
            calculator_add()
            return True
        if choice_location == 1:
            # Pout être étendue dessus à un autre temps
            return False

    print("Ce que tu a tapé n'est pas un option")
    return False
    pass


def calculator_add():
    number1 = input(bcolors.Yellow
                    + "C'est une calculatrice basique test qui vas te demander deux nombres et les additionner \n"
                    + "Premier nombre: ")

    number2 = input("Deuxième nombre: " + bcolors.RESET)

    result = float(number1) + float(number2)

    print(result)
    return result
    pass


main()

if checks() is True:
    print(bcolors.Yellow + "\nTout à marcher comme je l'attendais, comme je souhaitait, merveilleux\n" + bcolors.RESET)
    pass

elif checks() is False:
    print("\n" + "Quelque chose n'a pas marcher... Ou tu a juste dit non" + "\n")
    exit(0)

calculator_menu()

exit(1)
