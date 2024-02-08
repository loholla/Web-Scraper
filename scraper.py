import requests
from bs4 import BeautifulSoup
from pathlib import Path

articleFile = input("Enter the file name with the articles.\n") #Input for list of articles
if (Path(articleFile).is_file()): #Checks to make sure the user put in the path of a file
    articleList = open(articleFile, "r") #Opens the file and reads it
    articleNum = 0
    for URL in articleList.readlines():
        URL = str(URL[:-1]) #Removes the \n tag at the end of each URL

        articleNum = articleNum + 1
        articleName = "article_" + str(articleNum) + ".txt"
        article = open(articleName, "w", encoding="utf-8")

        #Goes to the address and gets the data from the server in the form of a response before saving it to the page variable
        page = requests.get(URL)
        #Takes the response given from requests.get and pulls out the html code using the html parser
        soup = BeautifulSoup(page.content, "html.parser")
        #Searches all of the HTML code to find p tags with the class "paragraph" and "inline-placeholder"
        elements = soup.find_all("p", class_="paragraph inline-placeholder")
        for element in elements:
            txt = element.text.strip() + "\n"
            article.write(txt)
        article.close()