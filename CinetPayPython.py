#!/usr/bin/env python
# coding: utf-8







import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go



PayIn = pd.read_excel('PayIn.xlsx')
PayIn.head()



PayOut = pd.read_excel('PayOut.xlsx')
PayOut.head()



Airtime = pd.read_excel('Airtime.xlsx')
Airtime.head()




# # Fusion des trois fichiers 



FusionDesDonnees = PayIn.append(PayOut).append(Airtime)




# Visualisation de notre data

FusionDesDonnees


# ## IMPUTATION DES VALEURS MANQUANTES
# 
# **Vue qu'au PayOut et au Airtime il n'y pas de commission(commission_opérateur et commission_Cinetpay) nous allons donc imputer par 0**

# #### Créons une fonction qui impute les valeurs manquantes




colnum = ('montant', 'commission_operateur','commission_cinetpay')
colnum




def imputmissingvalue(data, cols, val):
    valuesinput = dict.fromkeys(cols,val)
    data.fillna(valuesinput, inplace=True)
    return data



FusionDesDonnees = imputmissingvalue(FusionDesDonnees,colnum,0)
FusionDesDonnees.tail()


# ####  Créons une fonction pour formater en date



def dateformat(data, col):
    data[col] = pd.to_datetime(data[col], format='%Y-%m-%d %H:%M:%S')
    return data

#Appel de notre fonction
FusionDesDonnees = dateformat(FusionDesDonnees,'date_transaction')
FusionDesDonnees


# ### fonction qui tranforme le type d'une colonne en float
# 
# **Les données sont bien formatés dans notre cas mais nous formatons pour des cas critiques à venir**


def transtype(data, cols):
    for col in cols:
        data[col] = data[col].astype(np.float64)
    return data

FusionDesDonnees = transtype(FusionDesDonnees, colnum)
FusionDesDonnees.dtypes         


# # COMBINAISON DES FONCTIONS


def imputmissingvalue(data, cols, val):
    valuesinput = dict.fromkeys(cols,val)
    data.fillna(valuesinput, inplace=True)
    return data


def dateformat(data, col):
    data[col] = pd.to_datetime(data[col], format='%Y-%m-%d %H:%M:%S')
    return data

def transtype(data, cols):
    for col in cols:
        data[col] = data[col].astype(np.float64)
    return data

def traitement(data,cols,val):
    data = transtype(dateformat(imputmissingvalue(data,cols,val),'date_transaction'),cols)
    #data.drop_duplicates(keep = 'first', inplace=True)
    return data

    

FusionDesDonnees = traitement(PayIn.append(PayOut).append(Airtime),colnum,0)
FusionDesDonnees


FusionDesDonnees.dtypes



FusionDesDonnees['date_transaction'] = pd.to_datetime(FusionDesDonnees['date_transaction'])

# Définir les types pour chaque colonne
dtypes = {
    'montant': int,
    'commission_operateur': float,
    'commission_cinetpay': float,
    'date_transaction': 'datetime64'
}

# Enregistrer le DataFrame en XLSX avec les types définis
with pd.ExcelWriter(r'C:\Users\RCARINE\Desktop\CinetpayPython\CinetpayTestPython\ToutesLesTransactions.xlsx') as writer:
    FusionDesDonnees.to_excel(writer, sheet_name='ToutesLesTransactions', index=False, engine='openpyxl')





