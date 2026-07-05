from math import sqrt
from functools import reduce
import pandas as pd
import sys


def charger_donnees(chemin: str) -> pd.DataFrame:
    try:
        return pd.read_csv(chemin)
    except FileNotFoundError:
        print(f"Le fichier {chemin} n'existe pas.")
        sys.exit(1)

def nettoyer_donnees(df: pd.DataFrame) -> pd.DataFrame:
    return (df
        .assign(
            orientation = df["orientation"].str.strip().str.lower(),
            note        = pd.to_numeric(df["note"], errors="coerce"),
            heures_etudes = pd.to_numeric(df["heures_etudes"], errors="coerce")
        )
        .dropna(subset=["orientation", "note", "heures_etudes"])
    )



def calculer_bornes(df: pd.DataFrame) -> dict:
    return {
        "note_min"    : df["note"].min(),
        "note_max"    : df["note"].max(),
        "heures_min"  : df["heures_etudes"].min(),
        "heures_max"  : df["heures_etudes"].max(),
    }

def normaliser(valeur: float, minimum: float, maximum: float) -> float:
    if maximum == minimum:
        return 0.0
    return (valeur - minimum) / (maximum - minimum)

def normaliser_note(bornes: dict, note: float) -> float:
    return normaliser(note, bornes["note_min"], bornes["note_max"])

def normaliser_heures(bornes: dict, heures: float) -> float:
    return normaliser(heures, bornes["heures_min"], bornes["heures_max"])



def filtrer_groupe(df: pd.DataFrame, label: str) -> pd.DataFrame:
    return df[df["orientation"] == label]

def calculer_centroide(df: pd.DataFrame, bornes: dict) -> tuple:
    return (
        normaliser_note(bornes, df["note"].mean()),
        normaliser_heures(bornes, df["heures_etudes"].mean())
    )

def calculer_centroides(df: pd.DataFrame, bornes: dict) -> dict:
    return {
        label: calculer_centroide(filtrer_groupe(df, label), bornes)
        for label in df["orientation"].unique()
    }



def distance_euclidienne(point1: tuple, point2: tuple) -> float:
    return sqrt(sum(
        (a - b) ** 2
        for a, b in zip(point1, point2)
    ))

def predire(bornes: dict, centroides: dict, note: float, heures: float) -> dict:
    point = (
        normaliser_note(bornes, note),
        normaliser_heures(bornes, heures)
    )

    distances = {
        label: distance_euclidienne(point, centroide)
        for label, centroide in centroides.items()
    }

    prediction = min(distances, key=distances.get)
    total = sum(distances.values())

    confiance = (
        (total - distances[prediction]) / total * 100
        if total > 0 else 0.0
    )

    return {
        "prediction" : prediction,
        "confiance"  : confiance,
        "distances"  : distances,
    }


def evaluer(df: pd.DataFrame, bornes: dict, centroides: dict) -> float:
    resultats = map(
        lambda row: predire(bornes, centroides, row["note"], row["heures_etudes"])["prediction"] == row["orientation"],
        (row for _, row in df.iterrows())
    )

    correct = reduce(lambda acc, x: acc + (1 if x else 0), resultats, 0)

    return correct / len(df) * 100



def lire_float(message: str, minimum: float, maximum: float) -> float:
    while True:
        try:
            valeur = float(input(message))
            if minimum <= valeur <= maximum:
                return valeur
            print(f"Valeur invalide. Entrez un nombre entre {minimum} et {maximum}.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def saisir_eleve() -> tuple:
    note   = lire_float("Note en maths (0-20) : ", 0, 20)
    heures = lire_float("Heures d'étude par semaine (0-168) : ", 0, 168)
    return note, heures


def afficher_centroides(centroides: dict) -> None:
    print("\n--- Centroïdes ---")
    for label, (note, heures) in centroides.items():
        print(f"  {label:15} -> note: {note:.2f}, heures: {heures:.2f}")

def afficher_resultat(resultat: dict, fiabilite: float) -> None:
    print("\n--- Résultat ---")
    print(f"  Orientation prédite  : {resultat['prediction']}")
    print(f"  Confiance            : {resultat['confiance']:.2f}%")
    print(f"  Précision du modèle  : {fiabilite:.2f}%")
    print("\n  Distances :")
    for label, dist in resultat["distances"].items():
        print(f"    {label:15} : {dist:.4f}")



def main():
    # Pipeline de traitement
    df         = nettoyer_donnees(charger_donnees("data/eleves.csv"))
    bornes     = calculer_bornes(df)
    centroides = calculer_centroides(df, bornes)
    fiabilite  = evaluer(df, bornes, centroides)

    # Affichage des infos
    print(f"Labels trouvés : {list(centroides.keys())}")
    afficher_centroides(centroides)
    print(f"\nPrécision globale du modèle : {fiabilite:.2f}%")

    # Prédiction
    note, heures = saisir_eleve()
    resultat     = predire(bornes, centroides, note, heures)

    afficher_resultat(resultat, fiabilite)

if __name__ == "__main__":
    main()