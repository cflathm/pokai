from bs4 import BeautifulSoup
import requests 
import json
import time 

pokemon = {}
moves = {}

def get_base_stats():
    url = ("https://bulbapedia.bulbagarden.net/wiki/"
           "List_of_Pok%C3%A9mon_by_base_stats_(Generation_I)")
    data = requests.get(url)

    soup = BeautifulSoup(data.text, 'html.parser')

    table = soup.find("table")
    rows = table.findAll('tr')

    for row in rows[1:]:
        cells = row.find_all('td')
        Pid = int(cells[0].get_text().strip('\n'))
        Name = cells[2].get_text().strip('\n')
        Health = int(cells[3].get_text().strip('\n'))
        Attack = int(cells[4].get_text().strip('\n'))
        Defense = int(cells[5].get_text().strip('\n'))
        Speed = int(cells[6].get_text().strip('\n'))
        Special = int(cells[7].get_text().strip('\n'))
        pokemon[Pid] = {"Pid": Pid, 
                        "Name": Name, 
                        "Health": Health, 
                        "Attack": Attack, 
                        "Defense": Defense, 
                        "Speed": Speed, 
                        "Special":Special}
    


def get_typing():
    url = ("https://bulbapedia.bulbagarden.net/wiki/"
           "List_of_Pok%C3%A9mon_by_Kanto_Pok%C3%A9dex_number")
    data = requests.get(url)

    soup = BeautifulSoup(data.text, 'html.parser')

    tables = soup.findAll("table")
    
    for table in tables[1:4]:
        rows = table.findAll('tr')
        for row in rows[1:]:
            cells = row.findAll('td')
            Pid = int(cells[0].get_text().strip('\n')[2:])
            Type_1 = cells[4].get_text().strip('\n')
            if len(cells) > 5:
                Type_2 = cells[5].get_text().strip('\n')
            else:
                Type_2 = 'None'
            pokemon[Pid].update({"Type_1": Type_1, "Type_2":Type_2})

def get_learnsets():
    
    for Pid in range(1,152):
        #time.sleep(0.25)
        Curr_Pok = pokemon[Pid]["Name"]
        url = ("https://bulbapedia.bulbagarden.net/wiki/" +
               Curr_Pok + "_(Pok%C3%A9mon)/Generation_I_learnset")
        data = requests.get(url)
        soup = BeautifulSoup(data.text, 'html.parser')
        tables = soup.findAll("table")
        
        table = tables[0]
        for row in table.findAll("tr")[6:]:
            cells = row.findAll("td")
            Level = cells[0].get_text().strip('\n')
            Name = cells[1].get_text().strip('\n')    
            Type = cells[2].get_text().strip('\n')
            Power = cells[3].get_text().strip('\n')
            Accuracy = cells[4].get_text().strip('\n')[:-5]
            PP = cells[5].get_text().strip('\n')
            Move = {"Name": Name, 
                    "Level": Level,
                    "Type": Type,
                    "Power": Power,
                    "Accuracy": Accuracy,
                    "PP": PP}
            moves[Name] = Move            
    print(moves)
    exit()        
        

        

get_base_stats()
get_typing()
get_learnsets()
#print(pokemon)
