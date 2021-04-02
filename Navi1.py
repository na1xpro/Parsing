from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pprint import pprint
import requests

url_catalog = 'https://shop.navi.gg/ru/equipment'
page = requests.get(url=url_catalog).text
soup = BeautifulSoup(page, "html.parser")

url_list = soup.find_all('a', class_='btn product-item__btn')


for i in url_list:
    link = i.get('href')
    full_link = urljoin(url_catalog, link)

    page = requests.get(url=full_link).text
    soup = BeautifulSoup(page, "html.parser")

    title = soup.find('h1', class_="product__title").find("span").text
    photo_list = soup.find_all('a', class_='product-images__item')

    full_foto_product = []
    for photo_link in photo_list:
        link_photo = photo_link.get('href')
        full_foto_product.append(link_photo)

    price_1 = soup.find()
    price_list = {

    }

    variants = soup.find_all('input', class_='fn_variant')
    for variant in variants:
        name = variant.get('data-variant_name')
        size = variant.get('data-price')
        price_list.update({name: size})

    comment_name = soup.find('div', class_='comment__name').text.strip()
    comment_date = soup.find('div', class_='comment__date').text.strip()
    comment_text = soup.find('div', class_='comment__text-inner').text

    product = {
        'title': title,
        'image': full_foto_product,
        'price': price_list,
        'comment': {
            'name': comment_name,
            'date': comment_date,
            'text': comment_text,
        }
    }

    pprint(product)
    print()
