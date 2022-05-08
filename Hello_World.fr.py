def main():
    print("\"Hallo Monde!\"\n")

    is_exit = input("Ece que tu veux continuer tester ou terminer sa maintenant? (Vraie ou Faux): ")
    print("\n")

    if is_exit.lower() == "faux":
        exit(1)

    pass


# global y_or_n


def second():
    print("Hallo Monde! (pour la deuxième fois, tu as entrer dans un monde dans un autre monde)\n")
    name = input("Pouvez-vous taper votre nom pour le programe?: ")

    if name is None:
        print("Tu dois taper quelque chose! Donc pour ta paresse tu devras recommencer le programe pour continuer!")
        return False

    else:
        y_or_n = str(input("\nTon nom est " + name + ", correcte? (o or n): "))

    if y_or_n.lower() == "o" or y_or_n.lower() == "oui":
        return True

    elif y_or_n.lower() == "n" or y_or_n.lower() == "non":
        return False
    else:
        print("Ce que tu as taper n'est pas 'o' ni 'n', mais '" + y_or_n + "', cette réponse n'est pas supporter..."
              "\n\n")
        return False

    pass


def calculator_add():
    number1 = input("C'est une calculatrice basique test wqui vas te demander deux nombres et les additionner \n"
                    "Premier nombre: ")
    number2 = input("Deuxième nombre: ")
    result = float(number1) + float(number2)

    print(result)
    pass


main()

if second() is True:
    print("\n" + "Tout à marcher comme je l'attendais, comme je souhaitait, merveilleux" + "\n")
    pass

elif second() is False:
    print("\n" + "Quelque chose n'a pas marcher... Ou tu a juste dit non" + "\n")
    exit(0)

calculator_add()

exit(1)
