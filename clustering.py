import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import utils as ut
import os

def charger_donnees():
    df = pd.read_csv(ut.data_path)
    return df

def normaliser(df):
    scaler = MinMaxScaler()
    X = scaler.fit_transform(df[["note", "heures_etudes"]])
    return X

def methode_coude(X):
    inerties = []
    K_range = range(1, 11)
    
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X)
        inerties.append(kmeans.inertia_)
    
    # Graphique courbe du coude
    os.makedirs(ut.images_path, exist_ok=True)
    plt.figure(figsize=(8, 5))
    plt.plot(K_range, inerties, 'bo-')
    plt.xlabel("Nombre de clusters K")
    plt.ylabel("Inertie")
    plt.title("Méthode du coude")
    plt.savefig(ut.images_path + "coude.png")
    plt.show()
    
    return inerties

def appliquer_kmeans(X, k):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    return kmeans.labels_

def decrire_groupes(df, labels, k):
    df["groupe"] = labels
    
    print("\n" + "=" * 45)
    print("  DESCRIPTION DES GROUPES")
    print("=" * 45)
    
    for g in range(k):
        groupe = df[df["groupe"] == g]
        note_moy = groupe["note"].mean()
        heures_moy = groupe["heures_etudes"].mean()
        effectif = len(groupe)
        sci = (groupe["orientation"] == "Scientifique").sum()
        litt = (groupe["orientation"] == "Littéraire").sum()
        pct_sci = sci / effectif * 100
        pct_litt = litt / effectif * 100
        
        print(f"\nGroupe {g+1} :")
        print(f"   Effectif        : {effectif} élèves")
        print(f"   Note moyenne    : {note_moy:.2f} / 20")
        print(f"   Heures moyennes : {heures_moy:.1f} h/semaine")
        print(f"   Scientifique    : {pct_sci:.1f}%")
        print(f"   Littéraire      : {pct_litt:.1f}%")

def visualiser_clusters(df, k):
    couleurs = ["red", "blue", "green", "orange", "purple"]
    
    plt.figure(figsize=(8, 6))
    for g in range(k):
        groupe = df[df["groupe"] == g]
        noms_groupes = ["Eleves moyens", "Eleves performants", "Eleves en difficulté"]
        plt.scatter(
            groupe["heures_etudes"],
            groupe["note"],
            c=couleurs[g],
            label=f"Groupe {g+1}- {noms_groupes[g]}"  ,          alpha=0.6
        )
    
    plt.xlabel("Heures d'études")
    plt.ylabel("Note")
    plt.title("Clustering K-Means des élèves")
    plt.legend()
    plt.savefig(ut.images_path + "clusters.png")
    plt.show()

def main():
    print("=" * 45)
    print("  QUESTION 3 — CLUSTERING K-MEANS")
    print("=" * 45)
    
    # Chargement
    df = charger_donnees()
    
    # Normalisation
    X = normaliser(df)
    
    # Méthode du coude
    print("\nCalcul de la méthode du coude...")
    methode_coude(X)
    
    # Choix du K
    k = int(input("\nEntrez le K optimal que vous voyez sur le graphique : "))
    
    # K-Means
    labels = appliquer_kmeans(X, k)
    
    # Description
    decrire_groupes(df, labels, k)
    
    # Visualisation
    visualiser_clusters(df, k)
    
    print("\n >> Clustering terminé !")
    print(f" ++ Graphiques sauvegardés dans {ut.images_path}")

if __name__ == "__main__":
    main()