#!/home/jvo78226/eve_crest/venvcrest/bin/python
import pycrest
from pycrestHelpers import *

eve = pycrest.EVE()
eve()

"""
region = getByAttrVal(eve.regions().items, 'name', 'Catch')
print(region)
print()
item = getByAttrVal(getAllItems(eve.itemTypes), 'name', 'Tritanium').href
print(item)
print()
mkt = getAllItems(region().marketSellOrders(type=item))
print(mkt)
print()
"""




# debug my broken views with pycrest fixes
public_crest = pycrest.EVE()
public_crest()

# tranquility_user_count = public_crest().userCount_str
# print(tranquility_user_count)
"""
incursions = []
for thing_that_looks_like_a_dict_but_isnt in public_crest.incursions().items:
    incursion = {}
    for key, value in thing_that_looks_like_a_dict_but_isnt._dict.items():
        incursion[key] = value._dict if hasattr(value, '_dict') else value
    incursions.append(incursion)
print(incursions)
print()
"""
# inc = getAllItems(public_crest.incursions())
# same as the double nested for loop ^^
# print(inc)
# print()

"""
# debug my authed connection for workaround currently while refresh tokens are fixed
endpoint = pycrest.EVE()._authed_endpoint
type_id = 34          # Tritanium, the "Hello World" of EVE Items...
region_id = 10000002  # The Forge
type_url = "{0}inventory/types/{1}/".format(endpoint, type_id)
sell_orders_url = "{0}market/{1}/orders/sell/?type={2}".format(endpoint, region_id, type_url)
sell_orders = public_crest.get(sell_orders_url)['items']
print(sell_orders)
"""
