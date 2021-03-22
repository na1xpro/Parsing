from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

url_catalog = 'https://shop.navi.gg/ru/equipment'
page = requests.get(url=url_catalog).text
soup = BeautifulSoup(page, "html.parser")

url_list = soup.find_all('a', class_='btn product-item__btn')

# url_list = i.get('href')

for i in url_list:
    link = i.get('href')
    full_link = urljoin(url_catalog, link)

    page = requests.get(url=full_link).text
    soup = BeautifulSoup(page, "html.parser")

    title = soup.find('h1', class_="product__title").find("span").text
    photo_list = soup.find_all('a', class_='product-images__item')
    # print(title)
    for photo_link in photo_list:
        link_photo = photo_link.get('href')

    #     print(link_photo)
    # print()

    price_1 = soup.find()
    price_list = {

    }

    variants = soup.find_all('input', class_='fn_variant')
    for variant in variants:
        name = variant.get('data-variant_name')
        size = variant.get('data-price')
        price_list.update({name: size})

    # print(price_list)

    comment_name = soup.find('div', class_='comment__name').text
    comment_date = soup.find('div', class_='comment__date').text.strip()
    comment_text = soup.find('div', class_='comment__text-inner').text

    print(comment_text, comment_name, comment_date)

price = '//h1[@class="product__title"]/text()'
