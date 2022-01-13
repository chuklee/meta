# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 18:22:13 2022

@author: marti
"""
import re
import datetime,string, secrets
import gc #Va permettre de libérer de la mémoire une fois l'id et le password crée
import neurone
import sys
import mysql.connector

class Base:
    def __init__(self, taux_base, neurone_username, neurone_password, pc_dividende = 2):
        #Parametre de base
        #BASICS
        self.taux_base = taux_base #Représente l'investissement moyen prévue pour les différents neurones de la base
        self.pc_dividende = pc_dividende #Représente le pourcentage de dividende percu par la base chaque mois
        self.reserve = 0 #Reserve d'argent de la base pour les futurs investissement
        self.length = 1 #Nombre de neurones présent dans la base
        
        #NEURONES
        self.neurones = [] #Représente les différents neurones de la base
        first_member = neurone.Neurone(neurone_username, neurone_password,1) #Ici le premier neurone n'as pas de restrictions comparé à la sécurité de son mdp etc...
        self.neurones.append(first_member)
        
        #CREATION ID BASE
        current_day = datetime.datetime.now()
        part1 = str(current_day.strftime("%f"))
        part2 = str(current_day.strftime("%j"))
        part3 = str(current_day.strftime("%U"))
        part4 = str(current_day.strftime("%y"))
        identifiant = part1 + part2 + part3 + part4#Avec cette identifiant à 4 paramètres il y'a très peu de chance que un identifiant soit le meme en fonction des utilisateurs
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(20))
        
        #Sauvegarde des identifiants
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "popolo69",
            database = "baseid"
            )
        mycursor = mydb.cursor()
        sqlFormula = "INSERT INTO id (ID, Password) VALUES (%s,%s)"
        tosave = (identifiant, password)
        mycursor.execute(sqlFormula, tosave)
        mydb.commit()
        
        print("\nYour Base ID is : ", identifiant)
        print("Your password is : ", password)
        print("\n Save it to access to your base. There is no other way to connect to your base. If you forget it, you will not be able to recover it.")
        
        #CREATION ID BASE
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "popolo69",
            )
        mycursor = mydb.cursor()
        newdata = str("CREATE DATABASE base" + str(identifiant)) #Ici je suis obligé de mettre base devant car ca ne prend pas seulement les nombres meme si se sont des str de base
        mycursor.execute(newdata)
        mydb.commit()
        
        #Ici on remplis la database avec les éléments qu'on connait
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "popolo69",
            database = "base" + str(identifiant)
            )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE Basics (Parameters VARCHAR(255), Value FLOAT)")
        sqlFormula = "INSERT INTO Basics (Parameters, Value) VALUES (%s,%s)"
        Basics = [("taux_base", taux_base),
                    ("pc_dividende", pc_dividende),
                    ("reserve", 0),
                    ("length", 1)]
        mycursor.executemany(sqlFormula, Basics)
        mydb.commit()
        mycursor.execute("CREATE TABLE Neurones (Username VARCHAR(255), Password VARCHAR(255), pt_confiance INT, pt_vote FLOAT, valeur INT, rendement FLOAT)")
        sqlFormula = "INSERT INTO Neurones (Username, Password, pt_confiance, pt_vote, valeur, rendement) VALUES (%s,%s,%s,%s,%s,%s)"
        tosave = (str(neurone_username), str(neurone_password), 3, 1, 0, 0)
        mycursor.execute(sqlFormula, tosave)
        mydb.commit()
        #Clear les valeurs inutiles
        del identifiant
        del password
        del current_day
        del part1
        del part2
        del part3
        del alphabet
        gc.collect()
        
        
        
    def addmember(self, username, password, pt_confiance, pt_vote):
        total_pt_vote = 0 #Cette variable va permettre de vérifier que le total de pt de confiance avec l'ajout du nouveau membre sera bien égal à la len(neurones)
        for elt in self.neurones:
            current_username = elt.username
            total_pt_vote += elt.pt_confiance
            if(current_username == username): #Ici je regarde si le username n'est pas déja utilisé, si c'est le cas alors je raise une erreur
                raise NameError("Sorry but this username is already taken!")
                sys.exit()
    
        #Si je suis arrivée à cette étape alors le username n'existe pas, je passe donc à l'étape suivante.
        if(total_pt_vote + pt_vote != self.length):
            raise EnvironmentError("Sorry but this neurones has to much point of vote") #Ici ca ne marche pas car le nombre de point de vote doit être égal au nombre de neurone
            sys.exit()
        strong_password = False
        while not strong_password:
            if len(password) < 8:
                raise NameError("Make sure your password is at lest 8 letters")
            elif re.search('[0-9]',password) is None:
                raise NameError("Make sure your password has a number in it")
            elif re.search('[A-Z]',password) is None: 
                raise NameError("Make sure your password has a capital letter in it")
            else:
                strong_password = True
        #Le password est bon
            self.member.append(neurone.Neurone(username, password, pt_vote, pt_confiance))
