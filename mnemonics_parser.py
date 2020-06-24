'''
import requests
from bs4 import BeautifulSoup
import sys
import pandas as pd
import numpy as np

url = "https://mnemonicdictionary.com/"
#word = sys.argv[1]
word = 'accrue'
url = url+"?word="+word

final_list = []
pages = np.arange(1, 3, 1)
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

word_name = soup.find_all("div", attrs={"class": "media-heading"})
mnemonic_data = soup.find_all("div", attrs={"class": "card mnemonic-card"})
meaning_data = soup.find_all('div', attrs={'style':"padding-bottom:0px;"})


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


# to get the searched word 
word_name = word_name[0].get_text()
final_word_name = word_name.split()[-1].strip()

# to get all the mnemonics as a list
raw_mnemonics_data = mnemonic_data[1].get_text()
dirty_mnemonics_list = raw_mnemonics_data.split('\n')
#str_Mnemonics_list = list(filter(None, dirty_mnemonics_list))
#clean_list = [el.replace(u'\xa0',' ') for el in str_Mnemonics_list]

#mnemonics = clean_list[0].strip()
#upvotes = clean_list[2].split()[0]
#downvotes = clean_list[2].split()[1]

# get the meaning and synonyms
raw_meaning_data = meaning_data[0].get_text()
dirty_meaning_list = raw_meaning_data.split('\n')
clean_meaning_list = list(filter(None, dirty_meaning_list))

definition_list = [s for s in clean_meaning_list if "Definition" in s]
synonyms_list = [s for s in clean_meaning_list if "Synonyms" in s]

clean_definition_list = [defi.replace("Definition ","") for defi in definition_list]
synonyms_list = [syn.replace("Synonyms :","") for syn in synonyms_list]  
clean_synonyms_list = [x for xs in synonyms_list for x in xs.split(',')]
clean_synonyms_list = [a.strip() for a in clean_synonyms_list]

max_len = max(len(all_mnemonics_clean),len(clean_definition_list),len(clean_synonyms_list))


all_data={}

all_data ={"word":final_word_name,
            "mnemonics": all_mnemonics_clean,
            "upvotes":upvotes,
            "downvotes":downvotes,
            "definition":clean_definition_list,
            "synonym":clean_synonyms_list
            }


final_list.append(all_data)


df = pd.DataFrame.from_dict(all_data, orient='index')
df.transpose()



#print(mnemonic_data[0].find(class_="card-text").get_text())
print(all_data)
'''



import requests
from bs4 import BeautifulSoup
import sys
import pandas as pd
from time import sleep
from random import randint
import numpy as np

url = "https://mnemonicdictionary.com/wordlist/GREwordlist?page=6"
#word = sys.argv[1]
word = 'abate'
url = url+"?word="+word

final_list = []

#page = requests.get(url)
#soup = BeautifulSoup(page.content,'html.parser')
#movie_div = soup.find_all('div', class_='mb-2 mt-2')



    
        
  #page = requests.get("https://www.imdb.com/search/title/?groups=top_1000&start=" + str(page) + "&ref_=adv_nxt", headers=headers)
page = requests.get("https://mnemonicdictionary.com/wordlist/GREwordlist?page=" + '')
  
soup = BeautifulSoup(page.text, 'html.parser')
  
movie_div = soup.find_all('div', class_='mb-2 mt-2')
for container in movie_div:
    


    word_name = soup.find_all("div", attrs={"class": "media-heading"})
    mnemonic_data = soup.find_all("div", attrs={"class": "card mnemonic-card"})
    meaning_data = soup.find_all('div', attrs={'style':"padding-bottom:0px;"})
    
    all_mnemonics = []
    all_mnemonics = [item.find(class_='card-text').get_text() for item in mnemonic_data]
    all_mnemonics_clean = list(map(lambda s: s.strip(), all_mnemonics))
    
    
    up_down_votes_raw = []
    up_down_votes_raw = [item.find(class_='card-footer').get_text() for item in mnemonic_data]
    str_up_down_list = list(filter(None, up_down_votes_raw))
    up_down_votes_partial = []
    up_down_votes_partial = [el.replace(u'\xa0',' ') for el in str_up_down_list]
    
    up_down_votes_clean = list(map(lambda s: s.strip(), up_down_votes_partial))
    upvotes = []
    downvotes = []
    for i in up_down_votes_clean:
        aa = i.split()[0]
        bb = i.split()[1]
        upvotes.append(aa)
        downvotes.append(bb)
    
    
    		# to get the searched word 
    word_name = word_name[0].get_text()
    final_word_name = word_name.split()[-1].strip()
    
    # to get all the mnemonics as a list
    raw_mnemonics_data = mnemonic_data[1].get_text()
    dirty_mnemonics_list = raw_mnemonics_data.split('\n')
    		#str_Mnemonics_list = list(filter(None, dirty_mnemonics_list))
    		#clean_list = [el.replace(u'\xa0',' ') for el in str_Mnemonics_list]
    
    		#mnemonics = clean_list[0].strip()
    		#upvotes = clean_list[2].split()[0]
    		#downvotes = clean_list[2].split()[1]
    
    		# get the meaning and synonyms
    raw_meaning_data = meaning_data[0].get_text()
    dirty_meaning_list = raw_meaning_data.split('\n')
    clean_meaning_list = list(filter(None, dirty_meaning_list))
    definition_list = []
    definition_list = [s for s in clean_meaning_list if "Definition" in s]
    
    synonyms_list = [s for s in clean_meaning_list if "Synonyms" in s]
    clean_definition_list = []
    clean_definition_list = [defi.replace("Definition ","") for defi in definition_list]
    
    synonyms_list = [syn.replace("Synonyms :","") for syn in synonyms_list]
    clean_synonyms_list = []
    clean_synonyms_list = [x for xs in synonyms_list for x in xs.split(',')]
    clean_synonyms_list = [a.strip() for a in clean_synonyms_list]
    
    max_len = max(len(all_mnemonics_clean),len(clean_definition_list),len(clean_synonyms_list))
        
        
all_data = {}


 

		
all_data ={"word":final_word_name,
           "mnemonics": all_mnemonics_clean,
           "upvotes":upvotes,
           "downvotes":downvotes,
           "definition":clean_definition_list,
           "synonym":clean_synonyms_list
		          }









final_list.append(all_data)


#df = pd.DataFrame.from_dict(all_data, orient='index')
#df.transpose()
        


#print(mnemonic_data[0].find(class_="card-text").get_text())
print(final_list[0])
'''





