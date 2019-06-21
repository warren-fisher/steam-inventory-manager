import bs4 as bs
from requests.exceptions import HTTPError
import requests
import re
from ast import literal_eval

try: 
    response = requests.get('https://steamcommunity.com/market/listings/730/Prisma%20Case')

    response.raise_for_status()

except HTTPError as http_err:
    print(f"An HTTP error occured: {http_err}")

except Exception as err:
    print(f"Other error occured: {err}")
    
soup = bs.BeautifulSoup(response.content, 'lxml')

for script in soup.find_all('script'):
    print(script.text)

with open("./html.html", mode='wt', encoding='utf-8') as file:
    file.write(soup.prettify())

script_info = ''
for script in soup.find_all('script'):
    if 'var line1' in script.text:
        script_info = script.text

search = re.search('var line1(.+);', script_info)
pricing = literal_eval(search.group(1)[1:])

for pricing_window in pricing: 
    date = pricing_window[0]
    price = pricing_window[1]
    volume = pricing_window[2]

    print(f"{date} : {price} : {volume}")