import requests
from bs4 import BeautifulSoup


def get_formatted_text(element):
    return element.get_text().replace('\n', '')

web_url = "https://www.beagreatteacher.com/daily-fun-fact/page/"
user_agent = {'User-agent': 'Mozilla/5.0'}
data_result = []

for i in range(1,2):
    page_url = web_url + str(i)
    page = requests.get(page_url, headers = user_agent)
    soup = BeautifulSoup(page.content, 'html.parser')

    content = soup.find('main').find_all('p')
    date = get_formatted_text(soup.find('main').find('h1')).split('–')[1][1:]

    data = {
        "date": date,
        "thought": get_formatted_text(content[0]),
        "joke": get_formatted_text(content[1]),
        "fact": get_formatted_text(content[2]),
        "idea": get_formatted_text(content[3])
    } 

    data_result.append(data)

print(data_result)
