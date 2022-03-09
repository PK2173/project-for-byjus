import json
import requests
from bs4 import BeautifulSoup

def scraping(url_to_scrape):
    Solution_keys={}
    data= requests.get(url_to_scrape)
    soup=BeautifulSoup(data.text,'html.parser')
    try:
        answer=soup.find('div',class_="text_titleSolution__2t5ZU").get_text()
        if 'Solution' in answer:
            Solution_keys[url_to_scrape[-7:]]="True"
    except:
        Solution_keys[url_to_scrape[-7:]]="False"

    return Solution_keys




with open('project.json','w') as pro:
    data_list = ['1546465','1546500','1546921','1547009','1547160']
    cou=1
    for i in data_list:
        r=scraping(f"https://dev.byjusweb.com/question-answer/ques/?id={i}")
        json.dump(r,pro,indent=4)
        print(cou)
        cou+=1