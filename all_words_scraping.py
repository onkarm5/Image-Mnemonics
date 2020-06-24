import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

from time import sleep
from random import randint

#headers = {"Accept-Language": "en-US,en;q=0.5"}

all_words = []

#pages = np.arange(1, 472, 1)
pages = np.arange(1, 473, 1)
for page in pages: 
  #page = requests.get("https://www.imdb.com/search/title/?groups=top_1000&start=" + str(page) + "&ref_=adv_nxt", headers=headers)
  page = requests.get("https://mnemonicdictionary.com/wordlist/GREwordlist?page=" + str(page))
  
  soup = BeautifulSoup(page.text, 'html.parser')
  
  movie_div = soup.find_all('div', class_='mb-2 mt-2')
  
  sleep(randint(2,10))
  
  for container in movie_div:
      word = container.h2
      if word is not None:
          word = word.text
          all_words.append(word)
      else:
          pass
 
all_words_df = pd.DataFrame({'words':all_words})
     
print(all_words_df)
      