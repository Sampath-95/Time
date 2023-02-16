import requests
from bs4 import BeautifulSoup
import streamlit as st
# Making a GET request
r = requests.get('https://time.com/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Finding by id
s = soup.find('main', class_= 'homepage-wrapper')

# Getting the leftbar
leftbar = s.find('ul', class_='most-popular-feed__item-container')

# All the li under the above ul
lines = leftbar.find_all('li')
rb=s.find('ul', class_='tout__list items swipe-h')

rlines=rb.find_all('li')
col1, col2 = st.columns(2)

with col1:
	for r in lines:
		st.write(r.text)

with col2:
	for line in rlines:
		st.write(line.text)

