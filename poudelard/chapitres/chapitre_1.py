from poudelard.univers.personnage import initialiser_personnage, afficher_personnage
from poudelard.utils.input_utils import demander_texte, demander_nombre


def introduction():
    print("Bienvenue à Poudlard !")
    print("Ton aventure commence ici.")
    print("Prépare-toi à vivre une aventure pleine de découvertes,")
    print("ainsi que de choix importants et de mystères à percer !")


def creer_personnage():
    nom = demander_texte("Entrez le nom de votre personnage : ")
    prenom = demander_texte("Entrez le prénom de votre personnage : ")

    print("Choisissez vos attributs :")

    courage = demander_nombre("Niveau de courage (1-10) : ", 1, 10)
    intelligence = demander_nombre("Niveau d’intelligence (1-10) : ", 1, 10)
    loyaute = demander_nombre("Niveau de loyauté (1-10) : ", 1, 10)
    ambition = demander_nombre("Niveau d’ambition (1-10) : ", 1, 10)

    attributs = {
        "courage": courage,
        "intelligence": intelligence,
        "loyauté": loyaute,
        "ambition": ambition
    }

    joueur = initialiser_personnage(nom, prenom, attributs)

    afficher_personnage(joueur)

    return joueur
