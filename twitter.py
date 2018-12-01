#!/usr/bin/env python
#encoding: utf-8
# Author - Zezhong Wang
# Copyright from http://www.csdn.cn


import os
import shutil
import tweepy #https://github.com/tweepy/tweepy
import urllib.error
from urllib.error import HTTPError
import urllib.request


#Twitter API credentials (saved locally in env variable for security)
consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_key = os.environ.get('access_key')
access_secret = os.environ.get('access_secret')


def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    
    alltweets = []
    
    
    new_tweets = api.user_timeline(screen_name = screen_name, count = 20, include_rst = False, exclude_replies = True)
    
    
    alltweets.extend(new_tweets)
    
    
    oldest = alltweets[-1].id - 1
    
    
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name = screen_name, count = 20, max_id = oldest, include_rst = False, exclude_replies = True)
        
        alltweets.extend(new_tweets)
        
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print("...%s tweets downloaded so far" % (len(alltweets)))
        
    return alltweets


def getimage(image_url,path):
    for i, url in enumerate(image_url):
        try:
            urllib.request.urlretrieve(url, path+"/tpic"+str(i)+".jpg")
        except FileNotFoundError as err:
            print(err) 
        except HTTPError as err:
            print(err) 

def newdir(folder_name):
    path = os.getcwd()
    path = path + "/" + folder_name
    print (path)

    if not (os.path.isdir(path)):
        try:
            os.mkdir(path)
            print ("Directory %s successfully created" % path)            
        except OSError:
            print ("Directory %s could not be created" % path)
    else:
        shutil.rmtree(path)
        os.mkdir(path)
        print ("Directory %s cleared" % path)
    return path

