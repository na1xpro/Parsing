#by Nazar Dutka
#all code is copyrighted!!!

from bs4 import BeautifulSoup
import requests


def get_html(url):
    #   Get HTML CODE
    result = requests.get(url)
    return result.text


def get_data(html):
    #   Parser_info_player
    soup = BeautifulSoup(html, "lxml")
    name = soup.find("div", class_="name-player")
    nick = soup.find("div", class_='nickname-player')
    god_razhdenia = soup.find_all("span", class_="meaning-text")[1]

    strana = soup.find("span", class_="meaning-text")
    rol_v_komande = soup.find_all("span", class_="meaning-text")[2]
    game_skills = soup.find_all("span", class_="meaning-text")[3]
    info_player = soup.find("div", class_="description-player")
    photo_plaer = soup.find("div", class_="block-right").find("img").get("src")



    # Contacts

    facebook = soup.find("a", "item-network").get("href")
    vk = soup.find_all("a", class_="item-network")[1].get("href")
    tviter = soup.find_all("a", class_="item-network")[2].get("href")
    twitch = soup.find_all("a", class_="item-network")[3].get("href")
    steam = soup.find_all("a", class_="item-network")[4].get("href")
    instagram = soup.find_all("a", class_="item-network")[5].get("href")

    # Get Force

    print("Имя ---- " + name.text)
    print("Ник ---- " + nick.text)
    print("Город ---- " + strana.text)
    print("Год рождения ---- " + god_razhdenia.text)
    print("Роль в команде ---- " + rol_v_komande.text)
    print("Игровой опыт ---- " "c " + game_skills.text)
    print("Биография --- " + info_player.text)
    print("Фото ---- " +photo_plaer)


    print("Контакты >< ")
    print("Facebook ---- " + facebook)
    print("VK ---- " + vk)
    print("Tviter ---- " + tviter)
    print("Twith ---- " + twitch)
    print("Steam ----" + steam)
    print("Instagram ---- " + instagram)
    # #


def main():
    html = get_html("https://navi.gg/navi/players/34-s1mple")
    get_data(html)


if __name__ == '__main__':
    main()
