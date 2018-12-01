#Author by Zezhong Wang
# Copyright from https://www.w3schools.com/python/python_mysql_getstarted.asp
# Copyright from www.csdn.cn

import sys
import twitter as twitter
import video as video
import pymongo
import mysql.connector
import MongoDb as MongoDb
import MySQL as MySQL

from statistics import mode

def get_input_num():
    num=None
    while num is None:
        try:
            num = int(input("Type a number: "))
        except ValueError:
            print("Type a number")
    return num


MYSQL=1
def main():
   
    while(1):
    	mydb = mysql.connector.connect(
    		host = "localhost",
    		user = "username",
    		passwd = "passwd",
    		database = "mydatabase"
    		)
    	mycursor = mydb.cursor()
    	mycursor.execute("CREATE DATABASE if do not have mini3")
    	mycursor.execute("mini3")
    	mycursor.execute("CREATE TABLE  if do not have data (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(255), img_num VARCHAR(255),description VARCHAR(255),description_num VARCHAR(255))")
		mycursor.execute("use mini3")

        print("List:\n1.New user name\n2.Old user name\n3.Full database \n4.Delete DataBase\n5.Searching\n6.Exit")
        data=get_input_num();
        
        if (data == 1):
            MySQL.add(mycursor)
        elif(data == 2):
            print("Insert a DataBase:\n1.MySQL\n2.MongoDB")
            db = get_input_num()
            if (db == MYSQL):
                MySQL.user(mycursor)
            else:
                MongoDb.user()
		elif(data == 3):
            print("Insert a DataBase:\n1.MySQL\n2.MongoDB")
            db = get_input_num()
            if (db==MYSQL):
                MySQL.search(mycursor)
            else:
                MongoDb.search()

        elif(data == 4):
            MongoDb.delete()

        elif(data == 5):
            print("Insert a DataBase:\n1.MySQL\n2.MongoDB")
            db = get_input_num()
            if (db==MYSQL):
                MySQL.print(mycursor)
            else:
                MongoDb.print()

        elif(data==6):
            return
