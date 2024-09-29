# Rapport d'analyse

> Ewan Lansonneur
>
> Maxime Perrot
>
> Groupe 3C2
>
> R5.C.08 : Techniques d'IA
>
> B.U.T. Informatique 3
>
> IUT de Lannion
>
> Année scolaire 2024-2025
>
> Rédigé le 2024-09-27

## Introduction

Ce document est un rapport d'analyse d'un jeu de données dans le cadre de la ressource **R5.C.08 : Techniques d'Intelligence Artificielle** du BUT Informatique en vue de la préparation à la **SAE S5.C.01-S6.C.01**.

Cette ressource à pour objectif de démontrer qu'on peut mieux comprendre des données à l'aide d'outils et d'algorithmes d'analyse et de prédiction.

Pour ce projet des prérequis avait été établis pour le jeu de données qui serait exploité : 

 - Le jeu de données devait être composé de 100 individus minimum
 - Le jeu de données devait comporter 10 variables au minimum
 - Parmi ces variables 6 minimun devait être des variables quatitatives et 4 minimum devaient être qualitatives
  
Nous avons travaillé en binome en pair-programming.

## Présentation des données

Le jeu de données choisi est consitué des informations relatives à des personnages crées dans le cadre du jeu de rôle Donjons et Dragons 5e Edition. 

Ayant tout les deux une passion pour ce jeu de rôle nous avions tout de suite pensé à ce qu'il serait possible d'apprendre de données de masse.

Nous avons trouvé ces informations sur Kaggle après une recherche sur le sujet
Ces informations ont été recueilles sur une plateforme d'impression de fiche de personnage en ligne. 

La présence de nombreuses colonnes dans le fichier CSV original en fit un sujet de recherche idéal. Nous avions aussi des hypothèses en tête que nous voulions prouver ou réfuter grâce à cette analyse. 

Les individus composant ce dataset sont des 'personnages uniques', ceux ci sont des personnages ne partageant pas le même nom et classe en prenant la version du personnage ayant le plus haut niveau. Cela a pour objectif d'éviter de saturer le dataset avec un même personnage à différents niveaux.

Nous avons aussi nettoyé le dataset pour assurer l'intégrité des données étudiées.
Nous n'avons conservé que les fiches de personnages des classes officielles de la 5e édition.
Pour ce qui est des espèce des personnages nous n'avont conservé que celles ayant plus de 35 individus, au delà de cette limite apparaissait des options non-officielles. 
Aussi nous avons fusionné les fiches indiquant un version révisée de la classe de Ranger à l'originale dû à leur similitude.

Voici les variables que nous avons conservées :

Variable | Description
-|-
level | Niveau du personnage, valeur allant de 1 à 20
HP | *Health Points* les points de vie du personnage
AC | *Armor Class* la classe d'armure du personnage, indicateur de la resistance d'un personnage
Str | *Strength* la force physique du personnage
Dex | *Dexterity* l'adresse et l'agilité du personnage
Con | *Constitution* l'endurance, la santé et la force vitale du personnage
Int | *Intelligence* l'acuité mentale, la précision de la mémoire et la capacité à raisonner d'un personnage
Wis | *Wisdom* la sagesse et la perspicacité d'un personnage
Cha | **

## Analyse Quantitative

### Analyse en Composantes Principale (ACP)

## Analyse Qualitative

### Analyse Factorielle des Correspondances (AFC)

### Analyse de Correspondances Multiples (ACM)

## Conclusion