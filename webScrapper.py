from bs4 import BeautifulSoup
import requests

'''
Extrae su código html.
Obtén el título de la página <title>
Obtén todas las etiquetas <li> que contengan el siguiente atributo:
class="masthead-nav-topics-item"
Extrae el texto de la noticia limpio
'''
6
URL="https://www.xataka.com/espacio/nasa-va-a-recortar-presupuesto-hubble-su-salvacion-pasa-dos-multimillonarios-sector-privado"

page=requests.get(URL)
soup=BeautifulSoup(page.content,"html.parser")

allLiMarks=soup.find_all(name="li",class_="masthead-nav-topics-item")
pageText=page.text
pageTitle=soup.find_all(name="title")
pageContent=soup.find_all(class_="blob js-post-images-container")
# newsTextClean=

# print(page.text)
# print(allLiMarks)
# print(pageTitle)
print(pageContent)