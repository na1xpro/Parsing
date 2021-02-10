from bs4 import BeautifulSoup
import requests


def get_html(url):
    #   Get HTML CODE
    result = requests.get(url)
    return result.text


def get_data(html):
    #   Parser
    soup = BeautifulSoup(html, "lxml")
    name = soup.find("div", class_="name-player")
    nick = soup.find("div", class_='nickname-player')
    strana = soup.find("span", class_="meaning-text")
    info_player = soup.find("div", class_="description-player")
    photo_main = soup.find("div", class_='block-right').find("img")

    # Get Force

    # print("Имя ---- " + name.text)
    # print("Ник ---- " + nick.text)
    # print("Город ---- " + strana.text)
    # print("Биография --- "+info_player.text)

    # print("Фото ---- "+photo_main.text)


def main():
    html = get_html("https://navi.gg/navi/players/34-s1mple")
    get_data(html)


if __name__ == '__main__':
    main()
