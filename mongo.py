import pymongo
from pymongo import MongoClient
import certifi
from model import sentiment_analysis
ca = certifi.where()
cluster=MongoClient("mongodb+srv://khalil2022:1234@cluster0.yajye.mongodb.net/sentiment_analysis?retryWrites=true&w=majority",tlsCAFile=ca)
db=cluster['sentiment_analysis']
collection=db['sentiment_analysis']
def find(sentiment):
    list=[]
    tweets = collection.find({})
    for tweet in tweets:
        index=0
        for sen in tweet['sentiment']:
            if sen==sentiment:
                index=1
        if index==1:
            list.append(tweet['tweet'])
    return list
def add(tweet):
    json={
        'tweet':tweet,
        'sentiment':""
    }
    collection.insert_one(json)
    return 0
def add_sentiment():
    tweets = collection.find({})
    for tweet in tweets:
        if tweet['sentiment'] == "":
            id = tweet['_id']
            sentiment = sentiment_analysis(tweet['tweet'])
            collection.update_one({"_id": id}, {"$set": {"sentiment": sentiment}})
        else:
            print(tweet['sentiment'])
    return 0
def add_all(tweet,sentiment):
    json={
        'tweet':tweet,
        'sentiment':sentiment
    }
    collection.insert_one(json)
    return 0