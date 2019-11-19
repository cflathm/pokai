from bs4 import BeautifulSoup
import requests 
import json

pokemon = {}

def get_base_stats():
    url = ("https://bulbapedia.bulbagarden.net/wiki/"
           "List_of_Pok%C3%A9mon_by_base_stats_(Generation_I)")
    data = requests.get(url)

    soup = BeautifulSoup(data.text, 'html.parser')

    table = soup.find("table")
    rows = table.findAll('tr')

    for row in rows[1:]:
        cells = row.find_all('td')
        print(cells[0].get_text().strip('\n'))
        
    #print(table)


get_base_stats()