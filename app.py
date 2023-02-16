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

for r in rlines:
  st.write(r.text)
for line in lines:
	st.write(line.text)

