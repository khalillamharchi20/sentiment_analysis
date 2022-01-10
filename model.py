from tensorflow.keras.models import load_model
import joblib
import numpy
import math
from tensorflow.keras.preprocessing.sequence import pad_sequences
word2num=joblib.load('word2idx.pkl')
classes=joblib.load('class.pkl')
model=load_model('sentiment_analysis.h5')
def char_edit_tosequence(string):
    list=[]
    list2=[]
    string=string.lower()
    if string[-1]==".":
        string=string[:-1]
    for k in string.split(' '):
        try:
            list.append(int(word2num[k]))
        except:
            list.append(0)
    list2.append(list)
    list2=pad_sequences(list2,maxlen=29)
    return list2
def predict(list):
    return model.predict(list)
def index_max(list):
    index=0
    max=-math.inf
    for k in range(len(list)):
        for i in range(len(list[k])):
            if list[k][i]>max:
                index=i
                max=list[k][i]
    return classes[index]
def int_to_list(var):
    list=[]
    while var>0:
        list.append(var%10)
        var=var//10
    return list
def sentiment_analysis(tweet):
    tweet=char_edit_tosequence(tweet)
    tweet=predict(tweet)
    tweet = index_max(tweet)
    data={0:'optimistic',
          1:'thankful',
          2:'empathetic',
          3:'pessimistic',
          4:'anxious',
          5:'sad',
          6:'annoyed',
          7:'denial',
          8:'surprise',
          9:'Official report',
          10:'joking'}
    if tweet==10:
        return 'joking'
    else:
        tweet=int_to_list(tweet)
    for k in range(len(tweet)):
        tweet[k]=data[tweet[k]]
    return tweet
