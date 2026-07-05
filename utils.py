import unicodedata
from random import random

nom = "joyeux"
n = 200 #taille du dataset


def nom_f(nom):
    nom_sans_accents = unicodedata.normalize("NFKD", nom)
    nom_sans_accents = nom_sans_accents.encode("ascii", "ignore").decode("ascii")
    return f"data/{nom_f(nom)}.csv"

def gaine(nom_sans_accents: str) -> str:    
    nom_nettoye = "".join(c for c in nom_sans_accents if c.isalpha())
    seed = sum([ord(c) for c in nom_nettoye])
    return seed  


    



data_path = "data/eleves.csv"
images_path = "images/"
