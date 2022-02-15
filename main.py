# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:44:39 2022

@author: marti
"""
import neurone, base
import datetime
import sys
import mysql.connector


def loginbase(): #Attention la tu te login dans une base et non dans un neurone
    #Ici ca vérifie juste les id, la base n'est pas encore chargé dans python.
    connected = 0    
    identifiant = input("Please enter the id for your base : ")
    password = input("Please enter the password for your base : ")
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root", #↓Attention, pour éviter les attaques, il faut changer d'id et limiter le nb de connexion
    passwd = "popolo69",
    database = "baseid")
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM id")
    myresult = cursor.fetchall() #Pour print tout une colone
    for row in myresult:
        (secretid, secretpassword) = row
        if(secretid == identifiant and secretpassword == password):
            #Ici les identifiants sont bon, on va donc récupéré les info sur le serveur
            mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "popolo69",
            database = "base"+identifiant)
            cursor = mydb.cursor()
            #Ici on s'occupe des basics de la base, on fait les neurones après
            cursor.execute("SELECT Value FROM basics")
            myresult = cursor.fetchall()
            taux_base, pc_dividende, reserve, length = myresult
            taux_base = int(taux_base[0]) #Ici je fais ça car myresult est une liste de tuple
            pc_dividende = float(pc_dividende[0])
            reserve = float(reserve[0])
            length = int(length[0])
            #Ici on fait les neurones
            cursor.execute("SELECT * FROM neurones")
            records = cursor.fetchall()
            neurones = []
            for row in records:
                username, password, pt_confiance, pt_vote, valeur, rendement = row
                neurone_toappend = neurone.Neurone(username, password, pt_vote, pt_confiance, valeur, rendement)
                neurones.append(neurone_toappend)
            B = base.Base(taux_base, neurones[0].username, neurones[0].password, False, pc_dividende, neurones, reserve, length)
            return B
    while True:
        answer = input("Wrong Id or Password, if you want to retry type 1 else type 2 to return to the menu : ")
        if(answer == "1"):
            return loginbase()
        elif(answer == "2"):
            return "None"

def create_base(taux_base, username, password, connected):
    B = base.Base(taux_base, username, password)
    print("Your base is now create \n")
    connected = 1

def check_connect_neurone(base, user, password):
    """Will connect to a neurone of a base"""
    for neurone in base.neurones:
        if(neurone.username == user and neurone.password == password):
            return neurone
    return "None"


def connect_neurone(base, neurone):
    print("==Main menu==")
    print("What do you want to do")
    #TODO : faire un menu pour les neurones

def connect_base(base):
    """HEllO."""
    neurone_connect = False
    while True:
        print("== Main menu == ")
        print("What do you want to do")
        print("1 : Connect to a Neurone")
        print("2 : See the actual members")
        print("3 : See the actual repartition of the base")
        print("4 : Request to join the base")
        todo = input("Enter the number you want : ")
        if(todo == "1" and not neurone_connect):
            user = input("Please enter the username for your neurone : ")
            password = input("Please enter the password for your neurone")
            neurone_to_connect = check_connect_neurone(base, user, password)
            while(neurone_to_connect == "None"):
                print("Wrong username or password, please retry")
                user = input("Please enter the username for your neurone : ")
                password = input("Please enter the password for your neurone")
                neurone_to_connect = check_connect_neurone(base, user, password)
            print("You are now connected to " + neurone_to_connect.username)
            neurone_connect = True
        elif(todo == "1" and neurone_connect):
            print("You are already connected to a neurone")
        elif(todo == "2"):
            for i in range(len(base.neurones)):
                print(str(i+1) + " : " + base.neurones[i].username)
        elif(todo == "3"):
            #Check the repartition of pt_valeur of the base
            for i in range(len(base.neurones)):
                print(base.neurones[i].username + " : " + str(base.neurones[i].pt_valeur))
        elif(todo == "4"):
            print("You ask to join the base : ", base.identifiant)
            print("There is several things to do before you can join")
            print("Please enter the following informations")
            username = input("Username : ")
            password = input("Password : ")
            motivation = input("Motivation : ")
            pt_valeur = input("Pt_valeur you want : ")
            base.ask_to_join(username, password, motivation, pt_valeur)            


if __name__ == '__main__':
    while(True):
        connected = 0
        print("== Hello and welcome to META, what do you want to do ? : ==")
        print("1 : Login into a base")
        print("2 : Create a base")
        print("3 : Exit")
        todo = input("Enter the number you want :")
        while(todo != "1" and todo !="2" and todo != "3"):
            print("Sorry but your enter the wrong number")
            print("1 : Login into a base")
            print("2 : Create a base")
            print("3 : Exit")
            todo = input("Enter the number you want : ")
        if(todo == "1"):
            connected_base = loginbase()
            if(connected_base is not None):
                connect_base(connected_base)
            else:
                print("TODO")
        elif(todo == "2"):
            print("You choose to create a Base, if you never create on, please visit our website :  ")
            taux_base = input("Please enter your taux de base :     ")#Il faudra vérifier que c'est bien un entier (compris > 0 et < 100)
            pc_dividende_str = input("Please enter the percentage of dividende you want (if you type enter it will be 2%) :     ")
            if(pc_dividende_str == ""):
                pc_dividende = 2
            else:
                pc_dividende = int(pc_dividende_str) #Ici il faudrat vérifier que c'est bien un entier (> 0 et < 100)
            username = input("Please enter your username for your neurone :     ")
            password = input("Please enter your password for your neurone :     ")
            create_base(int(taux_base), username, password, pc_dividende)
        else:    
            sys.exit()#C'est le else