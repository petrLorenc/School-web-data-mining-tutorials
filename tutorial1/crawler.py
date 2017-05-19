import requests
from bs4 import BeautifulSoup
import time
 
header = {'user-agent': 'DDW'}
baseURL = 'http://localhost:8000'

def crawler():
    file= open("names.txt","w")
    frontier=[baseURL]
    crawled=[]
    while frontier:
        page=frontier.pop()
        try:
            print('Crawled:' + page)
            source = requests.get(page, headers=header).text

            soup=BeautifulSoup(source, "html5lib")
            links=soup.findAll('a',href=True)

            if  "person" in page:
                print (soup.findAll("div", { "class" : "person" }))
                file.write(str(soup.findAll("div", { "class" : "person" })))

            if page not in crawled:
                for link in links:
                    if link not in crawled:
                        frontier.append(baseURL + link['href'])
                crawled.append(page)

            time.sleep(1)
        except Exception as e:
            file.close()
            print(e)

    file.close()
 
crawler()