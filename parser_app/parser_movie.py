import requests
from bs4 import BeautifulSoup as BS

#ссылка для сайта которую мы парсим
URL = 'https://kinovibe.co/'

HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0",
}

def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

def get_data(html):
    bs = BS(html, features='html.parser')
    items = bs.find_all("div", class_='middle-content-wr clearfix')
    movie_list = []

    for item in items:
        title_tag = item.find("div", class_='custom1-title')
        if title_tag:
            title = title_tag.get_text(strip=True)
            movie_list.append({'title': title})

    return movie_list
    
def parsing_movie():
    response = get_html(URL)
    if response.status_code == 200:
        movie_list_2 = []
        for page in range(1, 3):
            response = get_html('https://kinovibe.co/genreserial/boevik/page/2/', params={'page':page})
            movie_list_2.extend(get_data(response.text))
        return movie_list_2
    else:
        raise Exception('error in parse')

# if __name__ == '__main__':
#     print(parsing_movie())

