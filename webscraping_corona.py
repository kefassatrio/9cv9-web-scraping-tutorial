import requests
import json
from bs4 import BeautifulSoup

user_agent = {'User-agent': 'Mozilla/5.0'}
page = requests.get("https://www.worldometers.info/coronavirus/country/indonesia/", headers = user_agent)

soup = BeautifulSoup(page.content, 'html.parser')

# To see the html
print(soup.prettify())

# To get a list of all h3 tags in the html
print(soup.find_all('h3'))

# To get the first h3 tag in the html
print(soup.find_all('h3')[0])

# you can also do this to get the same result 
# (find function automatically returns the first one that is found)
print(soup.find('h3'))

# you can get only the text using this function
print(soup.find('h3').get_text())

# You can find specific sections by finding the html tags using the html class
print(soup.find_all('div', class_='maincounter-number'))

main_counters = soup.find_all('div', class_='maincounter-number')
for counter in main_counters:
    print(counter.get_text().replace('\n', ''))

def get_formatted_text(element):
    return element.get_text().replace('\n', '')

cases = get_formatted_text(main_counters[0])
deaths = get_formatted_text(main_counters[1])
recovered = get_formatted_text(main_counters[2])

print("Corona cases: " + cases)
print("Deaths: " + deaths)
print("Recovered: " + recovered)

data = {
    'cases': cases,
    'deaths': deaths,
    'recovered': recovered
}

print("data: " + json.dumps(data))
