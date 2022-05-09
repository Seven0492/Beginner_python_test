class bcolors:
    Green = '\033[92m'  # GREEN
    Yellow = '\033[93m'  # YELLOW
    Red = '\033[91m'  # RED
    LIGHT_BLUE = "\033[1;34m"  # Blue
    RESET = '\033[0m'  # RESET COLOR


def main():
    print("\"" + bcolors.Green + "Hallo Monde!" + bcolors.RESET + "\"\n")

    is_exit = input(bcolors.Yellow + "Ece que tu veux continuer tester ou terminer sa maintenant?"
                    + bcolors.LIGHT_BLUE + " (Vraie ou Faux): " + bcolors.RESET)
    print("\n")

    if is_exit.lower() == "faux":
        exit(1)

    pass


# global y_or_n


def second():
    print(bcolors.Green + "Hallo Monde!" + bcolors.LIGHT_BLUE
          + " (pour la deuxième fois, tu as entrer dans un monde dans un autre monde)\n" + bcolors.RESET)

    name = input(bcolors.Yellow + "Pouvez-vous taper votre nom pour le programe?: " + bcolors.RESET)

    if name is None:
        print(bcolors.Yellow
              + "Tu dois taper quelque chose! Donc pour ta paresse tu devras recommencer le programe pour continuer!"
              + bcolors.RESET)
        return False

    else:
        y_or_n = str(input(bcolors.Yellow + "\nTon nom est " + bcolors.Green + name + bcolors.Yellow + ", correcte?"
                           + bcolors.LIGHT_BLUE + " (o or n): " + bcolors.RESET))

    if y_or_n.lower() == "o" or y_or_n.lower() == "oui":
        return True

    elif y_or_n.lower() == "n" or y_or_n.lower() == "non":
        return False
    else:
        print(bcolors.Yellow + "Ce que tu as taper n'est pas 'o' ni 'n', mais '" + bcolors.Green + y_or_n
              + bcolors.Yellow + "', cette réponse n'est pas supporter...\n\n")
        return False

    pass


def calculator_menu():
    print(bcolors.Yellow
          + "Sens toi chanceux(se), tu peux choisir entre 1 type de calcul avec deux nombres, fais ton choix")

    print(bcolors.LIGHT_BLUE + "1." + bcolors.Yellow + " Addition")

    choice = input("Make your choice: " + bcolors.RESET)

    print("\n")

    if choice == "1":
        calculator_add()
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

if second() is True:
    print(bcolors.Yellow + "\nTout à marcher comme je l'attendais, comme je souhaitait, merveilleux\n" + bcolors.RESET)
    pass

elif second() is False:
    print("\n" + "Quelque chose n'a pas marcher... Ou tu a juste dit non" + "\n")
    exit(0)

calculator_menu()

exit(1)
