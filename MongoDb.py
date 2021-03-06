# Author by Zezhong Wang
# Copyright from https://www.w3schools.com/python/python_mongodb_getstarted.asp
# Copyright from https://www.csdn.cn


import pymongo
import video as video
import twitter as twitter

def user():
    screen_name =input("Type user name ")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["users"]
    
    if (mycol.count()==0):
        print("No this name")
    else:
        for user in mycol.find():
            if (user.get('user')==screen_name):
                print(user)

def search():
    result = input("Type for search: ")
    print("Second customer",word,"description:")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["user"]

    dblist = myclient.list_database_names()
    if "mydatabase" in dblist:
    	print("The database exists.")

    for user in mycol.find():
        desc = user.get('description')
        desc = desc.split(',')
        if word in desc:
            print(user.get('user'))

def delete():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["user"]
    x = mycol.delete_many({})
    return

def print():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["user"]
    print("There are ",mycol.count(),"users at data base")
    print("The current data base is :")
    avg_im = 0
    desc = []
    for user in mycol.find():
        print(user)
        avg_im = avg_im + user.get('img_num')
        curr_des = user.get('description').split(',')
        for j in curr_des:
            desc.append(j)
    if (mycol.count() > 0):
        print("Some statistics:")
        print("The most popular description is",(max(set(desc), key = desc.count)))
        print("There is an average of",str(avg_im/mycol.count()),"images per feed")
    return