# Amazon.com დან Beauty & Personal Care - გვერდი
import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint

file = open('products.csv', 'w', encoding='utf-8', newline='\n')
csv_writer = csv.writer(file)
csv_writer.writerow(['Title', 'Price', 'Link'])

base_url = 'https://www.amazon.com/s?i=stripbooks&rh=n%3A283155&page='
page_num = 1
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

while page_num <= 5:
    url = f'{base_url}{page_num}'
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    products = soup.find_all('div', {'data-component-type': 's-search-result'})

    for product in products:
        title_elem = product.find('span', class_='a-text-normal')
        title = title_elem.text.strip()

        price_elem = product.find('span', class_='a-price-whole')
        price = price_elem.text.strip()

        link_elem = product.find('a', class_='a-link-normal')
        link = f"https://www.amazon.com{link_elem['href']}"


        csv_writer.writerow([title, price, link])
        print(f'Title: {title},\n Price: {price}$,\n Link: {link}\n')


    time.sleep(randint(15, 20))
    page_num += 1
file.close()










