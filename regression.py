import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

def main():
    df = pd.read_csv("data/eleves.csv")

    x = df["heures_etudes"]
    y = df["note"]

    plt.figure(figsize=(8,6))
    plt.scatter(x, y)

    a, b = np.polyfit(x, y, 1)
    x_line = np.linspace(x.min(), x.max(), 100)
    plt.plot(x_line, a*x_line+b, color="red", label=f"y = {a:.2f}x + {b:.2f}")

    plt.title("Relation entre les heures d'etude et la note")
    plt.xlabel("Heures d'etude")
    plt.ylabel("note")

    plt.grid(True)
    plt.savefig("figures/nuage_points.png")
    plt.show()

    correlation = x.corr(y)

    print("coefficient de correlation :", round(correlation, 3))

    a, b = np.polyfit(x, y, 1)
    print("pente :", a)
    print("ordonnee a l'origine :", b)

    r_squared = correlation**2
    print("R^2 :", round(r_squared, 3))

if __name__ == "__main__":
    main()
    
