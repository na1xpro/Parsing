from bs4 import BeautifulSoup
from lxml import html
import requests


def get_html(url):
    result = requests.get(url)
    return result.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')

    title = soup.find("h1", class_="product__title").text
    photo = soup.find("a", class_="product-images__item").get("href")

    options = soup.find_all('input', class_='fn_variant')
    Size_1 = {

    }
    for option in options:
        name = option.get('data-variant_name')
        size = option.get('data-price')

        Size_1.update({name: size})

    coments_name = soup.find("div", class_='comment__name').text.strip()
    comments_date = soup.find("div", class_='comment__date').text
    comment__text_inner = soup.find("div", class_='comment__text-inner').text.strip()

    print("Название  товара: " + title)
    print('Фото: \n' + photo, ' \nРазмер:Цена')
    print(Size_1)

    print("Имя: \n" + coments_name)
    print("Дата написания комента :" + comments_date)
    print("Коментарий: \n" + comment__text_inner)


def main():
    html = get_html('https://shop.navi.gg/ru/product/navi-mousepad-out-of-space')
    get_data(html)


if __name__ == '__main__':
    main()
