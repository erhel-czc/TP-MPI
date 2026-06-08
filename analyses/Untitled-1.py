# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

# %% [markdown]
# - Le numéro pour les colonnes correspond aux fréquences
# - modulus : stockage, l'autre c'est perte
# - attention, ajouter les titres
# - mettre en échelle log

# %%


def plot(data_name):
    df = pd.read_csv(f"{data_name}.csv", sep=";")

    freq = ["0,1", "1", "10"]
    temp = df["Temp(C)"]

    for f in freq:
        plt.plot(temp, df[f"Modulus {f}"], "-+", label=f"{f} Hz")

    plt.legend()
    plt.xlabel("Température (°C)")
    plt.ylabel("Module de stockage")

    plt.show()

    for f in freq:
        plt.plot(temp, df[f"Tan Delta {f}"], "-+", label=f"{f} Hz")

    plt.legend()
    plt.xlabel("Température (°C)")
    plt.ylabel("Tan Delta")

    plt.show()

    for f in freq:
        plt.plot(temp, df[f"Loss Modulus {f}"], "-+", label=f"{f} Hz")

    plt.legend()
    plt.xlabel("Température (°C)")
    plt.ylabel("Module de perte")

    plt.show()


# %%
plot("PMMA120 1deg")

# %%
plot("PMMA120 5deg")

# %%
plot("PMMA3500 1deg")

# %% [markdown]
# # étude énergies pmma120 1deg

# %%
plot("PMMA120 1deg")

# %%
