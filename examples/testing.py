# Import logic so that the inventoryapi module can be imported from up one directory without creating a package
from os import sys, path
sys.path.append(path.join(path.dirname(__file__), '..'))
from inventory_api import InventoryAPI as InvAPI

#import logging # for debug
#logging.basicConfig(level=logging.DEBUG) # Allows us to see the debugging, here purely for the example, if a request fails it is logged as ERROR

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

for key, value in items.items(): 
    print(f"{key} : {value}")

