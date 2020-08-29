import json
import requests
import lxml.html as parser

"""
   Freefire weapons stats
   by Sinf0r0s0 28/08/2020
   thanks to https://github.com/SwitchbladeBot/freefire-static-data
   
"""

html_text = requests.get('https://ff.garena.com/weapons/index/en/').content
tree = parser.fromstring(html_text)
html_on_script_tag = tree.xpath('//*[@id="weaponTpml"]/text()')[0]
weapon_elements = parser.fromstring(html_on_script_tag).xpath('li')


def get_info(n):
    name = n.xpath('./div/h4/span[1]/text()')[0]
    data = [int(n.xpath(f'./div/ul/li[{idx}]/div[2]/span[2]/text()')[0]) for idx in range(1, 9)]
    return name, data


weapons_dict = dict(map(get_info, weapon_elements))
print(weapons_dict)

with open('freefire_weapons_data.json', 'w') as outfile:
    json.dump(weapons_dict, outfile)
