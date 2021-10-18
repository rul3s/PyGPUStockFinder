#https://www.ldlc.com/es-es/informatica/piezas-de-informatica/tarjeta-grafica/c4684/+fv1766-9941,16762.html?sort=1

from selenium import webdriver
from bs4 import BeautifulSoup
from model import GPU
import pandas as pd
import unicodedata


def normalizePrice(readPrice):
    return readPrice.strip().replace('€', ',').replace(' ','')

def removeHtmlSpecials(text):
    return unicodedata.normalize("NFKD", text)

def main():
    gpu = []
    driver = webdriver.Chrome("C:\\chromedriver.exe")
    driver.get("https://www.ldlc.com/es-es/informatica/piezas-de-informatica/tarjeta-grafica/c4684/+fdi-1+fv1766-9941,16762.html?sort=1")

    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser", from_encoding="utf-8")
    for prod in soup.findAll('li', attrs={'class':'pdt-item'}):
        name=removeHtmlSpecials(prod.find('h3', attrs={'class':'title-3'}).find('a').getText())
        stock=removeHtmlSpecials(prod.find('div', attrs={'class':'stock'}).getText())
        price=normalizePrice(removeHtmlSpecials(prod.find('div', attrs={'class':'price'}).getText()))
        print(name ," -- ", stock ," -- ", price)
    

if __name__ == "__main__":
    main()


# print(
#     "Found product:\n"
#     "Name: " +name +"\n"
#     "Price: " +price +"\n"
#     "Stock: " +stock +"\n"
# )


#<div class="price">1&nbsp;700€<sup>95</sup></div>
#<div class="modal-stock-web pointer stock stock-1" data-stock-web="1"><span>En <em>stock</em></span>
# price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
# rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
# products.append(name.text)
# prices.append(price.text)
# ratings.append(rating.text)
