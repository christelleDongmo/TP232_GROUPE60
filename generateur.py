import numpy as np
import pandas as pd
import utils as ut
import os

def nom_vers_graine(nom):
    graine = 0
    for i, lettre in enumerate(nom):
        graine += ord(lettre) * (i + 1)
    return graine

def generer_donnees():
    graine = nom_vers_graine(ut.nomf)
    rng = np.random.default_rng(graine)

    heures = rng.integers(0, 30, ut.n)
    bruit = rng.normal(0, 2, ut.n)
    notes = 2 + 0.6 * heures + bruit

    notes = np.clip(notes, 0, 20).round(2)
    heures = np.clip(heures, 0, 30).astype(int)

    orientations = []
    for i in range(ut.n):
        proba = rng.random()
        if notes[i] >= 12 and heures[i] >= 10:
            orientation= "Scientifique" 
        else:
            orientation= "Littéraire" 
        orientations.append(orientation)

    df = pd.DataFrame({
        "ID": [f"E{i+1}" for i in range(ut.n)],
        "note": notes,
        "heures_etudes": heures,
        "orientation": orientations
    })

    return df, graine

def main():
    os.makedirs("data", exist_ok=True)

    df, graine = generer_donnees()
    df.to_csv(ut.data_path, index=False)

    sci = (df["orientation"] == "Scientifique").sum()
    litt = (df["orientation"] == "Littéraire").sum()

    print("=" * 45)
    print("  GÉNÉRATION DES DONNÉES")
    print(f"  Chef : {ut.nomf}")
    print(f"  Graine obtenue : {graine}")
    print("=" * 45)
    print(f"<< {ut.n} élèves générés")
    print(f":: Scientifique : {sci} élèves ({sci/ut.n*100:.1f}%)")
    print(f">> Littéraire   : {litt} élèves ({litt/ut.n*100:.1f}%)")
    print(f"== Données sauvegardées → {ut.data_path}")
    print("\nAperçu des 5 premières lignes :")
    print(df.to_string())

if __name__ == "__main__":
    main()