# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 16:47:38 2022

@author: marti
"""

import mysql.connector

class Server:
        
    def __init__(self, base, user, password, host = "localhost" ):
        self.base = base
        mydb = mysql.connector.connect( #Attention, ici il faudrat vérifier qu'il a bien le droit d'être la.
            host,
            user,
            password,
            base
            )
        self.cursor = mydb.cursor()
    
    
    def show_bases(self):
        self.cursor.execute("SHOW DATABASES")
        print("The different base who exist is :")
        for db in self.cursor:
            print(db)
            
    def add_data(self):
        if(self.base != "None"):
            raise AttributeError("Sorry but you are not loggin to a base")
        