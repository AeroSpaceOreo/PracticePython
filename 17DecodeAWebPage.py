# Exercise 17: Decode A Web Page
"""
Directions on installing modules for requests and bs4:
Locate the python script directory, there should be pip.py in it
~\Python\PythonXXXX\Scripts
Using windows command, run the following command:
~\Python\PythonXXXX\Scripts\pip install requests
~\Python\PythonXXXX\Scripts\pip install beautifulsoup4
pip install (module) is the command for DL and installing new modules
"""

import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
 
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())
