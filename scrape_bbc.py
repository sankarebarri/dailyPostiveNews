from bs4 import BeautifulSoup as bs
import requests

url = 'https://www.bbc.com/'
response = requests.get(url)
print(response.status_code)

soup = bs(response.content, 'html.parser')

titles = soup.find_all('a', {'class':'block-link__overlay-link'})
len(titles)

for title in titles:
    print(title.text.strip())

links = soup.find_all('a', href=True)
print(len(links))

all_links = []
for link in links:
    if (link['href'].startswith('http')) == False:
        all_links.append('https://bbc.com/'+link['href'])
    else:
        all_links.append(link['href'])
print(len(all_links))

print(all_links[:15])

news_link = []
for link in all_links:
    check_link = link.split('-')
    if link.split('-')[-1].isnumeric():
        #print(check_link)
        news_link.append(link)

news_link
len(news_link)

#mylist = list(set(mylist))
nnews_link = list(set(news_link))

len(nnews_link)

nnews_link

for link in nnews_link:
    response = requests.get(link)
    soup_1 = bs(response.content, 'html.parser')
    title = soup_1.find('h1')
    print(title.text)

bbc_news = []
for link in nnews_link:
    news_url = link
    response_2 = requests.get(news_url)
    #print(response_2.status_code)
    soup_1 = bs(response_2.content, 'html.parser')
    title = soup_1.find('h1').text
    articles = soup_1.find('article')
    #len(articles)
    try:
        contents = articles.find_all('p', {'class': 'ssrcss-1q0x1qg-Paragraph eq5iqo00'})
    except:
        print('Not found', link)
        title = 'No title'
    #len(contents)
    all_news = ''
    for content in contents:
        main_news = content.text
        all_news = all_news + main_news
        #print(main_news)
        if title == 'No title':
            all_news = 'No News'
        temporary = {
            'Link': link,
            'Title': title,
            'News': all_news,
        }
    bbc_news.append(temporary)

import pandas as pd
df = pd.DataFrame(bbc_news)

df.loc[13, 'News']

date_str = pd.to_datetime('today').strftime('%d-%m-%Y')
df.to_csv(f'bbc_{date_str}.csv')

pd.to_datetime('now')

pd.to_datetime('today').strftime('%m%d%Y')

df[:50]

df.loc[12, 'Link']
