def addieren(a, b):
    return a + b

def main():
    print("Taschenrechner")
    print("1 fuer Addition")
    print("2 fuer Subtraktion")
    print("3 fuer Multiplikation")
    print("4 fuer Division")

    wahl = input("Wahl eingeben: ")

    match wahl:
        case "1":
            a = float(input("Erste Zahl: "))
            b = float(input("Zweite Zahl: "))
            print("Resultat: {}".format(addieren(a, b)))
        case "2":
            a = float(input("Erste Zahl: "))
            b = float(input("Zweite Zahl: "))
            print("Resultat: {}".format(subtrahieren(a, b)))
        case "3":
            a = float(input("Erste Zahl: "))
            b = float(input("Zweite Zahl: "))
            print("Resultat: {}".format(multiplikation(a, b)))
        case "4":
            a = float(input("Erste Zahl: "))
            b = float(input("Zweite Zahl: "))
        case _:
            print("Falsche Auswahl, das Programm wird beendet.")

if __name__ == "__main__":
    main()
