# -*- coding: utf-8 -*-

"""
R5.C.08 : Techniques d'IA

TD 1 : ACP

Ewan Lansonneur 3C2
Maxime Perrot 3C2
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from biplot import biplot

# IMPORT DATA

#CSV_FILE = "data/csv/dnd_chars_unique.csv"
CSV_FILE = "data/tsv/dnd_chars_unique.tsv"

#data = pd.read_csv(CSV_FILE)
data = pd.read_csv(CSV_FILE, sep='\t')

# CLEAN UP DATA

df = pd.DataFrame(data)

x = df[['level','HP','AC','Str','Dex','Con','Int','Wis','Cha']]


# Standardisation des données
temp = x.sub(x.mean())
xscaled = temp.div(x.std())

pca = PCA(n_components = 2) # 3 car ça donne >50% selon le diagramme bâtons généré par le code ci dessous
pca_res = pca.fit_transform(xscaled)

L = list(pca_res)
for i,arr in enumerate(L):
    list_arr = list(arr)
    if list_arr[1] > 8:
        print(i, arr)

#-4.53 65.93
# Diagramme bâtons
# ----------------
y1 = list(pca.explained_variance_ratio_)
# x1=range(len(y1))
# plt.bar(x1,y1)
# plt.show()

#3.2 Graphique des variables
#Pour afficher le graphique des variables vous pouvez utiliser la fonction biplot1
#dans le fichier python ci-joint. Voici un exemple ci-dessous.

biplot(
    score = pca_res[:,0:2],
    coeff = np.transpose(
        pca.components_[0:2,:]
    ),
    cat          = y1[0:1],
    density      = False,
    coeff_labels = list(x.columns)
    )

# Graphique des individus
pcadf = pd.DataFrame(
    {
    "Dim1" : pca_res[:,0],
    "Dim2" : pca_res[:,1],
    "level" : df["level"],
    "HP" : df["HP"],
    "AC" : df["AC"],
    "Str" : df["Str"],
    "Dex" : df["Dex"],
    "Con" : df["Con"],
    "Int" : df["Int"],
    "Wis" : df["Wis"],
    "Cha" : df["Cha"]
    } 
)
pcadf.plot.scatter("Dim1","Dim2")
plt.xlabel("Dimension 1 (%)")
plt.ylabel("Dimension 2 (%)")
plt.suptitle("Premier plan factoriel (%)")
plt.show()


# for i, feature in enumerate():
#     plt.arrow(0, 0, pca.components_[0, i] * 3, pca.components_[1, i] * 3, color='black', head_width=0.05)
#     plt.text(pca.components_[0, i] * 3.2, pca.components_[1, i] * 3.2, feature, color='black')
    
