def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] = maisons[nom_maison] + points
        print(f"{nom_maison} gagne {points} points. Nouveau total : {maisons[nom_maison]}")
    else:
        print("Maison introuvable.")

def afficher_maison_gagnante(maisons):
    score_max = None
    for maison in maisons:
        if score_max is None or maisons[maison] > score_max:
            score_max = maisons[maison]

    gagnant = []

    for maison in maisons:
        if maisons[maison] == score_max:
            gagnant.append(maison)
    if len(gagnant) == 1:
        print("La maison gagnante est", gagnant[0], "avec", score_max, "points")
    else:
        print("Égalité entre les maisons suivantes avec", score_max, "points :")
        for maison in gagnant:
            print("--", maison)


def repartition_maison(joueur, questions):
    scores = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0 }

    def repartition_maison(joueur, questions):
        scores = {
            "Gryffondor": 0,
            "Serpentard": 0,
            "Poufsouffle": 0,
            "Serdaigle": 0
        }

        for question in questions:
            texte = question[0]
            choix_possibles = question[1]
            maisons_associees = question[2]

            print(texte)

            numero = 1
            for option in choix_possibles:
                print(f"{numero}. {option}")
                numero += 1

            choix = demander_nombre("Ton choix : ", 1, len(choix_possibles))
            maison = maisons_associees[choix - 1]

            scores[maison] += 3
            print()

        maison_gagnante = None
        score_max = None

        for maison in scores:
            if score_max is None or scores[maison] > score_max:
                score_max = scores[maison]
                maison_gagnante = maison

        attributs = joueur["Attributs"]

        if maison_gagnante == "Gryffondor":
            scores["Gryffondor"] += attributs["courage"] * 2
        elif maison_gagnante == "Serpentard":
            scores["Serpentard"] += attributs["ambition"] * 2
        elif maison_gagnante == "Poufsouffle":
            scores["Poufsouffle"] += attributs["loyauté"] * 2
        elif maison_gagnante == "Serdaigle":
            scores["Serdaigle"] += attributs["intelligence"] * 2

        print("Résumé des scores :")
        for maison in scores:
            print(f"{maison} : {scores[maison]} points")
        print()

        return maison_gagnante

