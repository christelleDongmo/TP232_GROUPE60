import subprocess
import sys

def main():
    print("=" * 45)
    print("  INF232 TP — Theme D : Etablissement scolaire")
    print("  Chef : DONGMO TCHUDZO Christelle Niquoize")
    print("  Groupe 60")
    print("=" * 45)

    nom = input("Entrez le nom du chefde groupe : ").strip().upper()
    import utils as ut
    ut.nomf = nom

    print("\n ÉTAPE 1 — Generation des donnees...")
    import generateur
    generateur.main()

    print("\n ÉTAPE 2 — Question 1 : Statistique univariee...")
    import descriptive
    descriptive.main()

    print("\n ÉTAPE 3 — Question 2 : Régression lineaire...")
    import regression
    regression.main()

    print("\n ÉTAPE 4 — Question 3 : Clustering K-Means...")
    import clustering
    clustering.main()

    print("\n ÉTAPE 5 — Question 4 : Classification supervisee...")
    import classification
    classification.main()

    print("\n" + "=" * 45)
    print("   Analyse complete terminee !")
    print("   Graphiques sauvegardes dans images/")
    print("=" * 45)

if __name__ == "__main__":
    main()