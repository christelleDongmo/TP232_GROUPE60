# INF232 – Travail Pratique

## Thème D : Établissement scolaire secondaire

### Description

Ce projet a été réalisé dans le cadre du cours **INF232**. Il met en œuvre différentes techniques d'analyse de données sur un jeu de données simulé représentant des élèves de Terminale.

Le programme permet de :

* générer un jeu de données à partir du nom du chef de groupe ;
* réaliser une analyse statistique descriptive ;
* étudier la relation entre les heures d'étude et les notes par régression linéaire ;
* identifier des profils d'élèves grâce à un clustering K-Means ;
* prédire automatiquement l'orientation scolaire d'un élève.

---

## Structure du projet

```text
.
├── app.py
├── generateur.py
├── descriptive.py
├── regression.py
├── clustering.py
├── classification.py
├── utils.py
├── data/
├── images/
└── rapport.pdf
```

---

## Prérequis

* Python 3.x

Bibliothèques Python :

* pandas
* numpy
* matplotlib
* scikit-learn

Installation :

```bash
pip install pandas numpy matplotlib scikit-learn
```

---

## Exécution

Lancer l'application avec :

```bash
python app.py
```

Le programme demande le nom du chef de groupe, génère automatiquement un nouveau jeu de données, exécute les quatre analyses demandées et enregistre les graphiques dans le dossier `images`.

---

## Résultats générés

Le projet produit automatiquement :

* le fichier des données (`data/eleves.csv`) ;
* un histogramme des notes ;
* une boîte à moustaches ;
* un nuage de points avec la droite de régression ;
* le graphique de la méthode du coude ;
* le graphique des clusters K-Means.

---

## Auteurs

**Groupe 60**

Chef de groupe : **DONGMO TCHUDZO Christelle Niquoize**

---

Pour plus de détails concernant la méthodologie, les résultats et les interprétations statistiques, consulter le rapport joint au projet.
