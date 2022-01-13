# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 16:47:38 2022

@author: marti
"""

import mysql.connector
"""
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "popolo69",
    database = "baseid"
    )
"""
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "popolo69"   )
mycursor = mydb.cursor()
sql = "DROP DATABASE "+ "base9357800120222" #Permet de delete la database à droite du +
mycursor.execute(sql)

#mycursor.execute("CREATE DATABASE BaseId")


"""
mycursor.execute("SELECT age FROM students")
# mycursor.execute("SELECT * FROM students") Va retourner tout le tableau
#myresult = mycursor.fetchone()
myresult = mycursor.fetchall() #Pour print tout une colone

for row in myresult:
    print(row) #ici c'est un tuple

"""
"""
Permet d'ajouter plusieurs data en meme temps dans un tableau

sqlFormula = "INSERT INTO students (name, age) VALUES (%s,%s)"
students = [("Bob", 19),
            ("Enna", 34),
            ("Mickael", 24),
            ("Martin", 20),
            ("Vincent", 98),]


mycursor.executemany(sqlFormula, students)


# mycursor.execute(sqlFormula, students) Commande si on veut ajouter qu'un seul élément et non une liste
"""
#mydb.commit() A utiliser que si on veut push qq chose


#mycursor.execute("CREATE TABLE ID (ID VARCHAR(255), Password VARCHAR(255))") #Permet de créer une table

"""
Permet de voir les différentes databases dans le serveur
mycursor.execute("SHOW DATABASES") #Permet d'executer des commandes comme dans le cmd

for db in mycursor:
    print(db)
"""