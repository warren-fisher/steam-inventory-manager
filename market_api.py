from bs4 import BeautifulSoup as bs
from requests.exceptions import HTTPError
import requests

try: 
    response = requests.get('https://steamcommunity.com/market/listings/730/Prisma%20Case')

    response.raise_for_status()

except HTTPError as http_err:
    print(f"An HTTP error occured: {http_err}")

except Exception as err:
    print(f"Other error occured: {err}")
    
soup = bs(response.content, 'html5lib')