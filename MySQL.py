# Author by Zezhong Wang
# Copyright from https://www.w3schools.com/python/python_mysql_getstarted.asp
# Copyright from www.csdn.cn

import mysql.connector
import twitter as twitter
import video as video


def user(mycursor):
    display_name = input("Type a user name: ")
    mycursor.execute("SELECT * FROM user_data WHERE username='"+display_name+"'")
    myresult = mycursor.fetchall()
    if (len(myresult) == 0):
        print("No this user name")
    else:
        for user in myresult:
            print(user)

def search(mycursor):
    word = input("Typer a word to find right oen: ")
    mycursor.execute(("SELECT * FROM user_data"))
    myresult = mycursor.fetchall()
    print("Second user already has this word",word,"in description:")
    for user in myresult:
        desc=user[3]
        desc=desc.split(',')
        if word in desc:
            print(user[1])

def print(mycursor):
    mycursor.execute(("SELECT * FROM user_data"))
    myresult = mycursor.fetchall()
    print("Here is ",len(myresult),"users at data base")
    print("The new data base is")
    avg_im=0
    desc=[]
    for user in myresult:
        avg_im=avg_im+int(user[2])
        curr_des=user[3].split(',')
        for x in curr_des:
            desc.append(x)
        print(user)
    if (len(myresult)>0):
        print(" description",(max(set(desc), key = desc.count)))
        print("Average string",str(avg_im/len(myresult)),"images per feed")
    return

def add(mycursor):
    display_name =input("Type a user name: ")
    mycursor.execute("SELECT * FROM user_data WHERE username='"+display_name+"'")
    myresult = mycursor.fetchall()
    if (len(myresult)!=0):
        print("User name already exsist")
        return
    print(display_name)
    print("Using twitter.py to download images" + diplay_name)
    img_num = twitter.twitter_from_user(display_name)
    print("creating video from ",str(img_num)," images")
    video.video(display_name)
    return


