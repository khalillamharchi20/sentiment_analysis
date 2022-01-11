import streamlit as st
import numpy as np
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
from mongo import find,add_sentiment
fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27)
st.title("twitter data vizualization")
st.sidebar.title("tweets")
sidebar_options = st.sidebar.selectbox(
    'options',
    (
            'overview',
        'charts'

    )
)

add_sentiment()

if sidebar_options == "overview":
    st.subheader("sentiment: annoyed")
    list = find('annoyed')
    data = {'tweet': list}
    df=pd.DataFrame(data)
    st.dataframe(df.head())
    st.subheader("sentiment: optimistic")
    list1 = find('optimistic')
    data1 = {'tweet': list1}
    df1 = pd.DataFrame(data1)
    st.dataframe(df1.head())
    st.subheader("sentiment: thankful")
    list2 = find('thankful')
    data2 = {'tweet': list2}
    df2 = pd.DataFrame(data2)
    st.dataframe(df2.head())
    st.subheader("sentiment: empathetic")
    list3 = find('empathetic')
    data3 = {'tweet': list3}
    df3 = pd.DataFrame(data3)
    st.dataframe(df3.head())
    st.subheader("sentiment: pessimistic")
    list4 = find('pessimistic')
    data4 = {'tweet': list4}
    df4 = pd.DataFrame(data4)
    st.dataframe(df4.head())
    st.subheader("sentiment: anxious")
    list5 = find('anxious')
    data5 = {'tweet': list5}
    df5=pd.DataFrame(data5)
    st.dataframe(df5.head())
    st.subheader("sentiment: sad")
    list6 = find('sad')
    data6 = {'tweet': list6}
    df6=pd.DataFrame(data6)
    st.dataframe(df6.head())
    st.subheader("sentiment: denial")
    list7 = find('denial')
    data7 = {'tweet': list7}
    df7=pd.DataFrame(data7)
    st.dataframe(df7.head())
    st.subheader("sentiment: surprise")
    list8 = find('surprise')
    data8 = {'tweet': list8}
    df8=pd.DataFrame(data8)
    st.dataframe(df8.head())
    st.subheader("sentiment: Official report")
    list9 = find('Official report')
    data9 = {'tweet': list9}
    df9 = pd.DataFrame(data9)
    st.dataframe(df9.head())
    st.subheader("sentiment: joking")
    list10 = find('joking')
    data10 = {'tweet': list10}
    df10 = pd.DataFrame(data10)
    st.dataframe(df10.head())
if sidebar_options=="charts":
    list = find('annoyed')
    list1 = find('optimistic')
    list10 = find('joking')
    list9 = find('Official report')
    list8 = find('surprise')
    list3 = find('empathetic')
    list2 = find('thankful')
    list4 = find('pessimistic')
    list5 = find('anxious')
    list7 = find('denial')
    list6 = find('sad')
    dataframe=[]
    dataframe=list+list1+list2+list3+list4+list5+list6+list7+list8+list9+list10
    sentiment=['annoyed' for k in list]+['optimistic' for k in list1]+['thankful' for k in list2]+['empathetic' for k in list3]+['pessimistic' for k in list4]+ ['anxious' for k in list5]+['sad' for k in list6]+['denial' for k in list7]+['surprise' for k in list8]+['Official report' for k in list9 ]+['joking' for k in list10]
    dataframe1={'tweet':dataframe,'sentiment':sentiment}
    dataframe2=pd.DataFrame(dataframe1)
    ax=sn.countplot(x='sentiment',data=dataframe2)
    st.pyplot(fig)