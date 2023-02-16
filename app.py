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
if btn:
  flag=1
  st.header("Latest Stories")
  for r in rlines:
    st.write(r.text)
