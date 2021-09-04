import requests
import pprint
from bs4 import BeautifulSoup

#print(soup.body.contents)
#print(soup.find_all('div'))
#print(soup.find('a'))
#print(soup.find_all('a'))
#print(soup.select('.score'))
#print(soup.select('#score_28405675'))
#print(links[0])
#print(votes[0].getText())


def votes_sorting(linkdict):
    return sorted(linkdict, key=lambda k:k['vote'], reverse=True)

def get_links_information(*args):
    links = args[0]
    subtext = args[1]
    page = args[2]

    link_list = []
    for index,link in enumerate(links):
            text =links[index].getText() 
            href =links[index].get('href',None)
            score = subtext[index].select('.score')
            if len(score):
                vote = int(score[0].getText().split(' ')[0])
                if vote > 99:
                    link_list.append({
                        'title': text,
                        'link': href,
                        'vote': vote,
                        'page':page
                    })
                    
    # sorted from the highest votes to lowest votes    
    return votes_sorting(link_list)

def pages_scraping_result(pagecount):
    counter = 1
    aggregated_list  = []
    # loop till it reach the number of pages
    while counter <= pagecount:
        res = requests.get(f'https://news.ycombinator.com/news?p={counter}')
        soup = BeautifulSoup(res.text,'html.parser')
        # get all classes with .storylink attribute
        links = soup.select('.storylink')
        #get all classes with .subtext attributes
        subtext = soup.select('.subtext')
        aggregated_list.append(get_links_information(links,subtext,counter))
        counter +=1

    return aggregated_list

pprint.pprint(pages_scraping_result(2))