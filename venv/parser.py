import requests
import math
from bs4 import BeautifulSoup
import csv
import pandas as pd


class Data:
    def __init__(self):
        self.URL = "https://slovopoisk.ru/type-1/length-5?page="

    def createBD(self):
        bd = []
        pages = (9576 / 100)
        for i in range(1, math.ceil(pages) + 1):
            page = requests.get(self.URL + str(i))
            soup = BeautifulSoup(page.content, "html.parser")
            elements = soup.find_all("span", class_="word-item")
            for element in elements:
                num = element.find("span", class_="word-num")
                s = str(element.text.strip())
                s1 = str(num.text.strip())
                bd.append(s.replace(s1, "").strip().lower())

        my_df = pd.DataFrame(bd)
        my_df.to_csv('bd.csv', index=False, header=False)
        print("The database has been created")

    @staticmethod
    def addData():
        with open('bd.csv', newline='') as f:
            reader = csv.reader(f)
            bdList = list(reader)
        return bdList

