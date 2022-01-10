import pymongo
from pymongo import MongoClient
import certifi
from model import sentiment_analysis
ca = certifi.where()
try:
 cluster=MongoClient("mongodb+srv://khalil2022:1234@cluster0.yajye.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=ca)
except:
 print('nothin')
db=cluster['sentiment_analysis']
collection=db['sentiment_analysis']
tweets=collection.find({})
for tweet in tweets:
 if tweet['sentiment']=="":
  id=tweet['_id']
  sentiment=sentiment_analysis(tweet['tweet'])
  collection.update_one({"_id":id},{"$set":{"sentiment":sentiment}})
 else:
  print(tweet['sentiment'])