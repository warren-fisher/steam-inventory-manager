# Import logic so that the inventoryapi module can be imported from up one directory without creating a package
from os import sys, path
sys.path.append(path.join(path.dirname(__file__), '..'))
from inventory_api import InventoryAPI as InvAPI
from market_api import MarketListing
from errors import MarketParsingError

import collections
import operator
from time import sleep

def order_items(items):
    sorted_items = sorted(items.items(), key=operator.itemgetter(1))
    return collections.OrderedDict(sorted_items)

def print_all(items):
    for key, value in items.items(): 
        print(f"{key} : {value}")

def print_cases(items):
    names = ['case', 'operation', 'capsule']
    print("item | quantity | unit price | total value")
    total_price = 0
    for item_name, count in items.items():
        for name in names:
            if name in item_name.lower():
                try:
                    # FIXME market price
                    listing = MarketListing(item_name)
                    price = listing.price()
                    total_price += price*count
                    print(f"{item_name} : {count} : {price} : {truncate_decimal(price*count)}")
                    sleep(5) # Try and prevent HTTP 429 errors
                except MarketParsingError:
                    print(f"Parsing ERROR {item_name} : {count} ")
                break

    print(f"{total_price=}")

def truncate_decimal(decimal):
    d = str(decimal)
    d = d.split(".")
    if len(d) == 1:
        return d[0]
    return int(d[0]) + 0.1 * int(d[1][0])

if __name__ == "__main__":
    import yaml 
    config = yaml.safe_load(open(r"examples/config.yaml"))

    inv = InvAPI()

    inv = inv.get(**config)

    items = {}
    for value, item in enumerate(inv):
        name = inv[value]['name']
        if name not in items:
            items[name] = 1
        else:
            items[name] += 1

    print_cases(order_items(items))