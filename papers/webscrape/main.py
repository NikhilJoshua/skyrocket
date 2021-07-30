import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.amazon.in/Test-Exclusive_2020_1139-Multi-3GB-Storage/product-reviews/B089MS8NW8/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber='

#url = 'https://www.google.com'

#r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 2})
cnt = 1
#df = pd.read_excel('testdata2.xlsx')
reviewlist = []

for i in range(1,13):
    r = requests.get(url+str(i))
    print(url+str(i))
    soup = BeautifulSoup(r.text, 'html.parser')
    reviews = soup.find_all('div', {'data-hook': 'review'})
    for item in reviews:
        review = {
            'title': item.find('a',{'data-hook': 'review-title'}).text.strip(),
            'rating': float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
            'body': item.find('span',{'data-hook': 'review-body'}).text.strip()
        }
        #print(review)
        reviewlist.append(review)

df = pd.DataFrame(reviewlist)
df.to_excel('testdata.xlsx', index=False)
print('fin')
