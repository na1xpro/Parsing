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
    size_M = soup.find_all("input", class_='fn_variant')[0].get("data-variant_name")
    size_L = soup.find_all("input", class_='fn_variant')[1].get("data-variant_name")
    price_M = soup.find_all("input", class_='fn_variant')[0].get('data-price').strip()
    price_L = soup.find_all("input", class_='fn_variant')[1].get('data-price').strip()

    Size_dict = {

    }
    Size_dict.update({size_M: price_M, size_L: price_L})

    coments_name = soup.find("div", class_='comment__name').text.strip()
    comments_date = soup.find("div", class_='comment__date').text
    comment__text_inner = soup.find("div", class_='comment__text-inner').text.strip()

    print("Название  товара: " + title)
    print('Фото: \n' + photo)
    print("Размеры и цена: \n" + size_M, '-' + price_M, '\n' + size_L, '-' + price_L)

    print("Имя: \n" + coments_name)
    print("Дата написания комента :" + comments_date)
    print("Коментарий: \n" + comment__text_inner)


def main():
    html = get_html('https://shop.navi.gg/ru/product/navi-mousepad-out-of-space')
    get_data(html)


if __name__ == '__main__':
    main()
