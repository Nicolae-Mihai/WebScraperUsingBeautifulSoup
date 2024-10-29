from bs4 import BeautifulSoup
import requests

'''
BeautifulSoup familiarization exercise.
'''

# URL of the page that we want to scraped.
URL="https://www.xataka.com/espacio/nasa-va-a-recortar-presupuesto-hubble-su-salvacion-pasa-dos-multimillonarios-sector-privado"

# We make a get request to the URL previously defined.
page=requests.get(URL)

# We parse the page content using BeautifulSoup.
soup=BeautifulSoup(page.content,"html.parser")

# Loading the HTML into pageHtml for an easyer reading.
pageHtml=soup

# Getting all "li" elements that whose class contains "masthead-nav-topics-item".
allLiMarks=soup.find_all(name="li",class_="masthead-nav-topics-item")

# Getting the page's title.
pageTitle=soup.title.get_text()

# Getting the article's story text.
pageContent=soup.find(class_="blob js-post-images-container").get_text()

# Print the results.
print(pageHtml)
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print(allLiMarks)
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print(pageTitle)
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print(pageContent)
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")