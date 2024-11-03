import requests as rq

from bs4 import BeautifulSoup

import pandas as pd

bUrl = 'https://books.toscrape.com/'

bHeader = {
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

bResp = rq.get(url=bUrl, headers=bHeader)

bSoup = BeautifulSoup(bResp.content, 'html.parser')

books = bSoup.find_all('article', attrs={'class':'product_pod'})

book_data = []

for book in books:
    title = book.find('h3').a['title']
    price = book.find('p', attrs={'class':'price_color'}).text
    rating = book.find('p', attrs={'class':'star-rating'})['class'][1]

    book_dict = {
        'title': title,
        'price': price,
        'rating': rating
    }

    book_data.append(book_dict)

   # print(book_data)

    print('title =', title)
    print('price =', price)
    print('rating =', rating)



book_dictdf = pd.DataFrame(book_data)
book_dictdf.to_csv('books.csv')