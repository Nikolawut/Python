import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def get_html(url):
    response = requests.get(url)
    return response.text

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    listings = soup.find_all('div', class_='thumb_div')
