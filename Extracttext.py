import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Give absolute path of the file
'''Format of csv 
    title 
    slug : Web URL to the artile
    blurb : short description
    body : HTML file
    category 
'''
df = pd.read_csv("./Data/vox-articles-Culture-806.csv")
print(df.head())
links = df.slug.to_list()
titles = df.title.to_list()

os.chdir("Data")
if not os.path.isdir("Culture"):
    os.mkdir("Culture")
os.chdir("Culture")


# for i in range(0,len(links)):
for i in range(0,350):
    url = links[i]
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    output = ''
    tag_list = [
        'p',
        # Tag that are required
    ]

    for t in text:
        if t.parent.name in tag_list:
            output += '{} '.format(t)

    f=open('C'+str(i+1),"w+")
    f.write(titles[i]+"\n")
    f.write(output)
    f.close()

    

