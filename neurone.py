# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 18:14:58 2022

@author: marti
"""

class Neurone:
    
    def __init__(self, username, password, pt_vote = 0, pt_confiance = 3, valeur = 0, rendement = 0):
        self.pt_confiance = pt_confiance #Les points de confiance permettent de définir a quel point on peux faire confiance à un neurone. Ceci augmente ou rétrécice en fonction de leurs résultat dans le mois.
        self.username = username #Le username du neurone
        self.password = password #Le password du neurone
        self.pt_vote = pt_vote #Les points de vote définissent l'influence du neurone sur la base. La somme des points de vote de la base est égal à la somme des neurones présent dans la base. Ces points permettent d'influer sur les différentes décisions de la base
        self.valeur = valeur #Compte du neurone (combien d'argent il détient dans la base). Ici il faudrat vérifier que l'argent reste bien dans le neurone et qu'il puisse pas faire de magouille.
        self.rendement = rendement #Formule à détermier en fonction du gain par rapport à l'argent investit et le temps depuis lequel il investit.
        