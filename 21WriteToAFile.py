# Exercise 21: Write To A File

# From Exercise 17: Decode A Webpage
import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

filename = '21WriteToAFile.txt'
open_file = open(filename, 'w') # r+ for readNwrite, r/w for read/write

headlines = ''

for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a:
        headlines += story_heading.a.text.strip() + '\n'
        print(headlines)
                              
open_file.write(headlines)
open_file.close()

print('-----Contents saved to ' + filename + '------')


###Alternative###
"""
with open(filename, 'w') as open_file
open_file.write('A string to write')
"""
###Suit for single write. This exercise, it's better to close all at once
###Since there's a multiple writes
        
