import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import datetime
from time import sleep
from random import randint

#headers = {"Accept-Language": "en-US,en;q=0.5"}

def get_page(url):
    response = requests.get(url)
    
    # Check if download was sucessful
    if response.status_code != 200:
        raise Exception('Unable to download page {}'.format(url))
    
    # Get the page HTML
    page_content = response.text
    
    # Create a bs4 doc
    doc = BeautifulSoup(response.text, 'html.parser')
    return doc

def write_csv(data, filepath='./dags/temp/'):

    filename = 'adorocinema_'+ datetime.now().strftime('%Y_%m_%d_%H_%M_%S')+'.csv'
    filepath = filepath+filename 
    keys = data[0].keys()
    with open( filepath, 'w+', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)


def  mnemonic_scraper_all ( page_quantity ):
    final_data  =   []
    for  page  in  range ( 0 , page_quantity ):
      final_data  +=  scraping_avaliacao_adoro_cinema ( page )

    write_csv ( final_data )

def scraping_avaliacao_adoro_cinema ( page_number ):
    ind_dict = {}
    final_data = []
    url = 'https://mnemonicdictionary.com/wordlist/GREwordlist?page=' + str(page_number)
    modified_soup = get_page(url)
    mnemonic_div = modified_soup.find_all('div', class_='mb-2 mt-2')
    for container in movie_div:
      word = container.find_all("h2")
      
      definition = str(container . find( "div" , attrs={'style':"padding-bottom:0px;"} ))
      clean_definition =definition[definition.find('<br/>')+len('<br/>'):definition.rfind('<div style="padding-top:8px;')]

      mnemonic_data = container.find_all("div", attrs={"class": "card mnemonic-card"})
      all_mnemonics = [item.find(class_='card-text').get_text() for item in mnemonic_data]
      all_mnemonics_clean = list(map(lambda s: s.strip(), all_mnemonics))

      up_down_votes_raw = [item.find(class_='card-footer').get_text() for item in mnemonic_data]
      str_up_down_list = list(filter(None, up_down_votes_raw))
      up_down_votes_partial = [el.replace(u'\xa0',' ') for el in str_up_down_list]
      up_down_votes_clean = list(map(lambda s: s.strip(), up_down_votes_partial))
      upvotes = []
      downvotes = []
      for i in up_down_votes_clean:
          aa = i.split()[0]
          bb = i.split()[1]
          upvotes.append(aa)
          downvotes.append(bb)
      
      
      ind_dict["word"] = word
      ind_dict["definition"] = clean_definition
      ind_dict["mnemonics"] = all_mnemonics_clean
      ind_dict["upvotes"] = upvotes
      ind_dict["downvotes"] = downvotes

      final_data.append(ind_dict)

    return final_data


