

def calculator():

    Zahl = float(input("Geben sie eine Zahl ein: "))
    Zahl2 = float(input("Geben sie eine Zahl ein: "))

    Operator = input("Geben sie Plus/ Minus/ Mal oder Geteilt ein: ")

    if Operator == "Plus":

        Ergebnis = Zahl + Zahl2
        print(Ergebnis)
        return

    elif Operator == "Minus":

        Ergebnis = Zahl - Zahl2
        print(Ergebnis)
        return

    elif Operator == "Mal":

        Ergebnis = Zahl * Zahl2
        print(Ergebnis)
        return


    elif Operator == "Geteilt":

        Ergebnis = Zahl / Zahl2
        print(Ergebnis)
        return

    else:

        Operator = ""

        print("Eingabe ungültig bitte geben sie Plus Minus Mal oder Geteilt ein: ")
        return

calculator()