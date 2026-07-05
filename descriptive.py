import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


# Lecture de donnees
df = pd.read_csv("data/eleves.csv")

notes = df["note"]

print("STATISTIQUES DESCRIPTIVES")

print(f"effectifs : {len(notes)}")
print(f"moyenne : {notes.mean():.2f}")
print(f"minimum : {notes.min():.2f}")
print(f"maximum : {notes.max():.2f}")
print(f"mediane : {notes.median():.2f}")
print(f"variance : {notes.var():.2f}")
print(f"ecart-type : {notes.std():.2f}")

Q1 = notes.quantile(0.25)
Q2 = notes.quantile(0.50)
Q3 = notes.quantile(0.75)

print(f"Q1 : {Q1:.2f}")
print(f"Q2 :{Q2:.2f}")
print(f"Q3 :{Q3:.2f}")

print(f"Ettendue : {notes.max()-notes.min():.2f}")

IQR = Q3-Q1
print(f"IQR : {IQR:.2f}")

borne_inf = Q1-1.5*IQR
borne_sup = Q3+1.5*IQR
outliers = df[(notes < borne_inf) | (notes > borne_sup)]

print("\nvaleurs aberrantes :")
print(outliers)

plt.figure(figsize=(8,5))
plt.hist(notes, bins=10)
plt.title("Histogramme des notes")
plt.xlabel("notes")
plt.ylabel("nombres d'eleves")

plt.savefig("data/histogramme_notes.png")
plt.show()

plt.figure(figsize=(6,3))
plt.boxplot(notes, vert=False)
plt.title("Boite a moustaches des notes")
plt.savefig("data/boxplot_notes.png")
plt.show()
