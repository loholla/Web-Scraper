import requests 
from bs4 import BeautifulSoup as bs

# Takes the URL provided by the user, then requests.get takes the URL and grabs all of the HTML code and stores it in the variable page
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = bs(page.content, "html.parser")