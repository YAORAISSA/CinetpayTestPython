Après le traitement de nos différents fichiers reçu avec Excel et Powerbi, nous avons automatisé ces différents traitements effectués sur Excel et Powerbi avec un script Python.

L'écriture de ce script est décrit dans ce README.




# Bibliothèques installées

nous avons installé :

**Pandas** pour la lecture et manipulation(traitement) des fichiers
**Numpy** pour les calculs mathématiques
**Pyplot** pour la visualisation des données
**pandas_profiling** est une bibliothèque qui permet de faire une analyse descriptives des données

# Description du contenu du dossier

**CinetPayPython.ipynb** correspond au notebook qui a été utilisé pour la partie exploratoire et test de notre projet

**CinetPayPython.py** c'est le script qui contient la partie automaisée de notre travail

**ToutesLesTransactions.xlsx** correspond à la source finale utilisée pour la conceptions du tableau de board dans Powerbi

Les fichiers avec l'extension **html** sont les résultats des analyses exploratoires effectuées sur les différents fichiers (Airtime, PayIn, PayOut, ToutesLesTransactions).



# Creation de fonction qui permettent de faire différents traitements

**imputmissingvalue()** permet d'imputer les valeur manquante de notre data car après fusion des différents fichier nous remarquons que le fichier PayIn à deux colonnes de plus à savoir commission_cinetpay et commission_operateur que PayOut et Airtime et donc nous avions des valeurs manquantes d'où la necessité de les imputer.

**dateformat()** permet le formatage de la colonne date en format date

**transtype()** permet de changer le type des valeurs d'une colonne car les colonnes montant,commission_cinetpay et commission_operateur et date_transaction n'avais pas les types adéquats

**traitement()** est une fonction qui englobe toute les fonctions précedentes 


# Fusion des 3 fichiers 

**FusionDesDonnees** est le nom de la variable contenant les trois fichiers fusionné à l'aide de append qui est une fonction de pandas.


# Démarrage du script

étape 1: appuyer sur windows r et saisir "cmd" et faire entrée

étape 2: utiliser la commande "cd" pour se rendre dans le dossier du projet en étant dans la console 

étape 3: saisir la commande "python CinetPayPython.py"

Utilisé le fichier **ToutesLesTransactions** généré comme source dans Powerbi.

# Observations

Lors de la phase exploiratoire nous observé que notre jeu de données contenait des étant données que nous n'avions toutes les informations du point de vue métier nous jugé bon de ne pas les supprimer dans la suite de nos travaux mais nous avons écrit le code qui permet de les supprimers s'il s'avère que ce sont de vrais doublons.


