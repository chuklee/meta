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
            return identifiant
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


def connect(connected, base, neurone):
    if(not connected):
        raise ValueError("Sorry but you are not connected")
        sys.exit()#Je sais pas si ca exit de base donc je fais ici, à verifier.
    while True:
        print("== Main menu == ")
        print("What do you want to do")
        print("1 : Add a Member to the base")
        todo = input("Enter the number you want:    ")
        if(todo == "1"):
            print("You choose to add a member to a base")
        else:
            print("Sorry but you enter a wrong number, please try again.")
            print("Return to the menu...")
if __name__ == '__main__':
    while(True):
        connected = 0
        print("Hello and welcome to META, what do you want to do ? :")
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
            baseid = loginbase()
            if(baseid != "None"):
                connected = 1
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