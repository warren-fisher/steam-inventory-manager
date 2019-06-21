import bs4 as bs
from requests.exceptions import HTTPError
import requests
import re
from ast import literal_eval

# TODO: Currently pricing info is always in USD$
# The following link is an example of how the currency can be set to rubles,
# however, I am not sure if setting language to russian is neccessary
# https://steamcommunity.com/market/listings/730/Prisma%20Case?l=russian&cc=ru

class MarketListing:
    
    def __init__(self, item_name):
        self.name = item_name
        self.url = f'https://steamcommunity.com/market/listings/730/{self.name}'

        self.parse()

    def get_response(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response

    def parse(self):
        response = self.get_response()
        soup = bs.BeautifulSoup(response.content, 'lxml')

        for script in soup.find_all('script'):
            if 'var line1' in script.text:
                text = script.text

        search = re.search('var line1(.+);', text)
        string_representation_of_list = search.group(1)[1:]

        self.pricing_history = literal_eval(string_representation_of_list)

    def price(self):
        price_now_index = len(self.pricing_history) - 1
        return self.pricing_history[price_now_index][1]

if __name__ == "__main__":
    m = MarketListing('Prisma Case')
    print(m.price())