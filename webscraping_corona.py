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
# [<h3>Total Coronavirus Cases in Indonesia</h3>, <h3>Daily New Cases in Indonesia</h3>, 
# <h3>Active Cases in Indonesia</h3>, <h3>Total Coronavirus Deaths in Indonesia</h3>, 
# <h3>Daily New Deaths in Indonesia</h3>]

# To get the first h3 tag in the html
print(soup.find_all('h3')[0])
# <h3>Total Coronavirus Cases in Indonesia</h3>

# you can also do this to get the same result of soup.find_all('h3')[0]
# (find function automatically returns the first elemet that is found)
print(soup.find('h3'))
# <h3>Total Coronavirus Cases in Indonesia</h3>

# you can get only the text using this function
print(soup.find('h3').get_text())
# Total Coronavirus Cases in Indonesia

# You can find specific sections by finding the html tags using the html class
print(soup.find_all('div', class_='maincounter-number'))
# [<div class="maincounter-number">\n<span style="color:#aaa">349,160 </span>\n</div>, 
# <div class="maincounter-number">\n<span>12,268</span>\n</div>, <div class="maincounter-number" style="color:#8ACA2B ">\n
# <span>273,661</span>\n</div>]

main_counters = soup.find_all('div', class_='maincounter-number')
for counter in main_counters:
    print(counter.get_text())
"""
349,160 


12,268


273,661
"""

def get_formatted_text(element):
    return element.get_text().replace('\n', '')

main_counters = soup.find_all('div', class_='maincounter-number')
cases = get_formatted_text(main_counters[0])
deaths = get_formatted_text(main_counters[1])
recovered = get_formatted_text(main_counters[2])

print("Corona cases: " + cases)
print("Deaths: " + deaths)
print("Recovered: " + recovered)
# Corona cases: 349,160 
# Deaths: 12,268
# Recovered: 273,661


main_counters = soup.find_all('div', class_='maincounter-number')
cases = get_formatted_text(main_counters[0])
deaths = get_formatted_text(main_counters[1])
recovered = get_formatted_text(main_counters[2])

data = {
    'cases': cases,
    'deaths': deaths,
    'recovered': recovered
}

json_data = json.dumps(data)

print("data: " + json_data)
