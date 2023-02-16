import requests
from bs4 import BeautifulSoup
import streamlit as st
r = requests.get('https://time.com/')

soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('main', class_= 'homepage-wrapper')

rb=s.find('div',class_="partial latest-stories")

rlines=rb.find_all('li')
flag=0
btn=st.button('Get Stories')
li=[]
for r in rlines:
  li.append(r.text)
if btn:
  flag=1
  st.header("Latest Stories")
  j=1
  for r in li:
    st.write(str(j)+'. '+r)
    j+=1
