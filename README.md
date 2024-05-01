# Tableau de Bord - Population Équine en France

Ce tableau de bord interactif a été développé dans le cadre d'un projet réalisé lors de la formation en data analyst. Il vise à explorer la population équine en France à travers des visualisations interactives et des analyses approfondies. Le jeu de données utilisé provient du Répertoire National des Équidés, répertoriant tous les équidés ayant vécu en France depuis 1960. 

## Données Utilisées

Le jeu de données utilisé est le fichier des équidés du SIRE (Système d'Informations Répertoriant les Équidés) daté du 9 février 2023, disponible sur [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/fichier-des-equides/#/resources). Il est au format CSV et répertorie les équidés enregistrés en France depuis 1976. Le fichier comporte 4 091 566 lignes pour 8 variables, notamment la race, le sexe, la date de naissance, le pays de naissance, le nom, l'autorisation à la consommation humaine, et la date de décès.

## Visualisations Disponibles

1. **KPI - Nombre de Chevaux en France à l'Instant T :** ✅
2. **KPI - Âge Moyen des Chevaux :** ✅
3. **Graphique en Camembert - Proportion des Sexes :** ✅
4. **Histogramme - Proportion des Races (Principales) :** ✅
5. **Graphique en Courbe - Nombre de Naissances par Mois par Année :** ✅
6. **Nuage de Mots - Noms les Plus Utilisés :** ✅

## Description du Travail

Mon objectif principal était de comprendre en profondeur l'état actuel de la population équine en France et d'explorer sa diversité sous différents angles. J'ai réalisé ce travail en utilisant Python et la bibliothèque Streamlit pour créer un tableau de bord interactif.

J'ai débuté en analysant le nombre total de chevaux enregistrés en France, qui s'élevait à 482 797 au 9 février 2023. Ensuite, j'ai calculé l'âge moyen des chevaux, révélant une moyenne élevée de 18,85 ans, ce qui est notable compte tenu de l'espérance de vie moyenne des chevaux.

En explorant la répartition des sexes, j'ai observé une nette prédominance des juments et des étalons, ce qui reflète les pratiques d'élevage. Le graphique en histogramme a mis en évidence la diversité des races équines en France, avec une grande proportion de races inconnues, ajoutant ainsi une dimension de variété à la population équine.

L'analyse des naissances par mois et par année a révélé des tendances saisonnières, avec un pic de naissances en janvier, principalement lié à la présence de chevaux de courses. Des baisses significatives du nombre de naissances au cours de la dernière décennie ont été observées, probablement influencées par des facteurs économiques et sociétaux.

Enfin, une exploration des noms les plus couramment donnés aux chevaux a apporté une touche légère à l'analyse, révélant des choix tels que "Princesse" ou "Caline", souvent attribués aux poneys et aux chevaux d'instruction.

## Conclusion

Ce tableau de bord offre une vue complète et interactive de la population équine en France. Il met en lumière la prédominance des juments et étalons, l'âge moyen élevé des chevaux, les tendances saisonnières des naissances, ainsi que la diversité des races et des noms. Ces analyses fournissent des insights essentiels pour les professionnels du secteur équin et les passionnés de chevaux.
