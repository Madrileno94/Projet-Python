def demander_texte(message):
    while True:
        texte = input(message).strip()
        if texte != "":
            return texte
        else:
            print("Veuillez entrer un texte non vide.")

def demander_nombre(message, min_val=None, max_val=None):

    valide = False

    while not valide:
        saisie = input(message).strip()
        valide = True


        if saisie == "":
            print("Veuillez entrer un nombre entier valide.")
            valide = False
        else:

            negatif = False
            start = 0

            if saisie[0] == "-":
                negatif = True
                start = 1


                if len(saisie) == 1:
                    print("Veuillez entrer un nombre entier valide.")
                    valide = False


            if valide:
                for c in saisie[start:]:
                    if c < '0' or c > '9':
                        print("Veuillez entrer un nombre entier valide.")
                        valide = False

            if valide:
                nombre = int(saisie)

                # Vérification min
                if min_val is not None and nombre < min_val:
                    print(f"Veuillez entrer un nombre ≥ {min_val}.")
                    valide = False

                # Vérification max
                if max_val is not None and nombre > max_val:
                    print(f"Veuillez entrer un nombre ≤ {max_val}.")
                    valide = False

    return nombre

def demander_choix(message, options):


