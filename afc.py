# -*- coding: utf-8 -*-

"""
R5.C.08 : Techniques d'IA

TD 2 : AFC

Ewan Lansonneur 3C2
Maxime Perrot 3C2
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from sklearn.decomposition import PCA
from sklearn.decomposition import FactorAnalysis
from sklearn.preprocessing import StandardScaler
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from mca import MCA

INLINE_TAG_SEPARATOR = "|"
ACCEPTED_CLASSES = [
    "Artificer",
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard",
]

ACCEPTED_RACES = [
    "Human",
    "Half-Elf",
    "Wood Elf",
    "Dragonborn",
    "Tiefling",
    "Half-Orc",
    "Mountain Dwarf",
    "High Elf",
    "Tabaxi",
    "Lightfoot Halfling",
    "Hill Dwarf",
    "Forest Gnome",
    "Goliath",
    "Goblin",
    "Dark Elf",
    "Warforged",
    "Firbolg",
    "Protector Aasimar",
    "Turtle",
    "Rock Gnome",
    "Kobold",
    "Lizardfolk",
    "Triton",
    "Kenku",
    "Stout Halfling",
    "Minotaur",
    "Variant",
    "Ghastly Halfling",
    "Deep Gnome",
    "Fallen Aasimar",
    "Orc",
    "Bugbear",
    "Fire Genasi",
    "Scourge Aasimar",
    "Serpentblood",
    "Shadow Elf",
    "Changeling",
    "Aarakocra",
    "Water Genasi",
]
# Choice based on most common chosen races above a threshold

# IMPORT DATA

CSV_FILE = "data/tsv/dnd_chars_unique.tsv"

data = pd.read_csv(CSV_FILE, sep="\t")

#######################################
# CLEAN UP DATA #
#######################################

df = pd.DataFrame(data)

x = df[["race", "justClass"]]

# Remove multiclass (lines with "|" in justClass)
x = x[
    ~x["justClass"].str.contains("|", regex=False)
]  # if regex not false, will interpret '|' as 'or' operator

# Merge Ranger and Revised Ranger
x["justClass"].replace("Revised Ranger", "Ranger", inplace=True)

# Remove non-core classes
x = x[x["justClass"].isin(ACCEPTED_CLASSES)]

# Remove blacklisted races
x = x[x["race"].isin(ACCEPTED_RACES)]

## Accepted races : Sort by most used races
# x['count'] = x.groupby('race')['race'].transform('count')
# x = x.drop_duplicates('race')
# print(x.sort_values('count', ascending=False).to_string())

#######################################
# Getting Number of factors#
#######################################

data_crosstab = pd.crosstab(x["race"], x["justClass"])

temp = data_crosstab.sub(data_crosstab.mean())
data_scaled = temp.div(data_crosstab.std())

chi_square_value, pvalue = calculate_bartlett_sphericity(data_scaled)

n_factors_max = min(data_scaled.shape) - 1

n_factors = 3

fa = FactorAnalyzer(n_factors=n_factors_max, rotation=None)
fa.fit(data_scaled)
ev, v = fa.get_eigenvalues()

# Eigenvalues / Factors graph
# plt.scatter(range(1,data_scaled.shape[1]+1),ev)
# plt.plot(range(1,data_scaled.shape[1]+1),ev)
# plt.title('ScreePlot')
# plt.xlabel('Factors')
# plt.ylabel('Eigenvalue')
# plt.grid()
# plt.show()

################################################
# Analyse Factorielle des Correspondance (AFC) #
################################################

methods = [
    (
        "FANorotation",
        FactorAnalysis(
            3,
        ),
    ),
    ("FAVarimax", FactorAnalysis(3, rotation="varimax")),
    ("FAQuartimax", FactorAnalysis(3, rotation="quartimax")),
]

fig, axes = plt.subplots(ncols=3, figsize=(10, 8), sharex=True, sharey=True)
for ax, (method, fa) in zip(axes, methods):
    fa = fa.fit(data_scaled)
    components = fa.components_
    vmax = np.abs(components).max()
    ax.scatter(components[0, :], components[1, :])
    ax.axhline(0, -1, 1, color="k")
    ax.axvline(0, -1, 1, color="k")
    for i, j, z in zip(components[0, :], components[1, :], data_scaled.columns):
        ax.text(i + 0.02, j + 0.02, str(z), ha="center")
    for i, j, z in zip(components[0, :], components[1, :], data_scaled.index):
        ax.text(i - 0.02, j - 0.02, str(z), ha="center")
    ax.set_title(str(method))
    if ax.get_subplotspec().is_first_col():
        ax.set_ylabel("Factor1")
    ax.set_xlabel("Factor2")

plt.tight_layout()
plt.show()

###############################################
# Analyse des correspondances multiples (ACM) #
###############################################


dc = pd.DataFrame(pd.get_dummies(x[["race", "justClass"]]))
dc.head()
mcaFic = MCA(dc, benzecri=False)
plt.scatter(mcaFic.fs_c()[:, 0], mcaFic.fs_c()[:, 1])
for i, j, nom in zip(mcaFic.fs_c()[:, 0], mcaFic.fs_c()[:, 1], dc.columns):
    plt.text(i, j, nom)
plt.show()
