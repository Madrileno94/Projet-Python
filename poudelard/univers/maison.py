def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] = maisons[nom_maison] + points
        print(f"{nom_maison} gagne {points} points. Nouveau total : {maisons[nom_maison]}")
    else:
        print("Maison introuvable.")



