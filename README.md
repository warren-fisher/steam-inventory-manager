# steam-inventory-manager
Command-line tool to list the contents of one or many steam accounts

## Main features
- Python implementation of getting steam inventory for any game/contextid, with matching descriptions
- Python 3 supported
- In-built filter for tradable or non-tradable items
- Proxy support, supports a list of socks/http/etc proxies, automatically cycles them with customisable values (how many repeats for same proxy)
- Retries and customisable values for retry (retry delay, number of retries)
- Optional debug logging

## Changes from before
- Syntax is different, please look at example.py and adjust accordingly!
- Proxies are now in a list and get cycled, unlike before where you could only have 1 proxy
- Retries added
- Timeout param added
- count/language options added
- Optional debug mode added

## Mentions
- The API used for fetching the inventory get's full credit to itsjfx/python-steam-inventory-api

## Requirements
See requirements.txt

## Proxy info
Needs requests[socks] which will install pysocks to allow proxies to work for socks proxies

For proxies it uses anything python requests supports under its proxies param, socks5 and http have been tested to work

## Examples
See examples/example.py