import re
from ast import literal_eval

import requests
from requests.exceptions import HTTPError

import bs4 as bs
from errors import MarketParsingError

from time import sleep

# TODO: Currently pricing info is always in USD$
# The following link is an example of how the currency can be set to rubles,
# however, I am not sure if setting language to russian is neccessary
# https://steamcommunity.com/market/listings/730/Prisma%20Case?l=russian&cc=ru

class MarketListing:
    
    def __init__(self, item_name):
        self.name = item_name
        self.url = f'https://steamcommunity.com/market/listings/730/{self.name}'

        if not self.parse():
            raise MarketParsingError

    def get_response(self):
        response = requests.get(self.url)
        try: 
            response.raise_for_status()
            return response
        except HTTPError: 
            if response.status_code == 429: # Requests are too frequent
                sleep(60)
                return self.get_response()
            return response

    def parse(self):
        """
        If the data can be parsed as expected, 
        return the pricing_history as well as set the class attribute pricing history.
        If the data is not as expected return False
        """
        response = self.get_response()
        soup = bs.BeautifulSoup(response.content, 'lxml')

        for script in soup.find_all('script'):
            if 'var line1' in script.text:
                text = script.text

        try:
            search = re.search('var line1(.+);', text)
            string_representation_of_list = search.group(1)[1:]

            self.pricing_history = literal_eval(string_representation_of_list)
            return self.pricing_history

        except NameError:
            return False

    def price(self):
        price_now_index = len(self.pricing_history) - 1
        return self.pricing_history[price_now_index][1]

if __name__ == "__main__":
    m = MarketListing('Prisma Case')
    print(m.price())