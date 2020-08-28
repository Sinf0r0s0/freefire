import json
import requests
import lxml.html as parser

"""
   Freefire weapons stats
   by Sinf0r0s0 28/08/2020
   thanks to https://github.com/SwitchbladeBot/freefire-static-data
   
"""

html_texto = requests.get('https://ff.garena.com/weapons/index/en/').content
tree = parser.fromstring(html_texto)
infos_na_tag_script = tree.xpath('//*[@id="weaponTpml"]/text()')[0]
armas_elem = parser.fromstring(infos_na_tag_script).xpath('li')


def get_info(n):
    _nome = n.xpath('./div/h4/span[1]/text()')[0]
    _data = [n.xpath(f'./div/ul/li[{idx}]/div[2]/span[2]/text()')[0] for idx in range(1, 9)]
    return _nome, _data


armas_dict = dict(map(get_info, armas_elem))
print(armas_dict)

with open('freefire_armas_data.json', 'w') as outfile:
    json.dump(armas_dict, outfile)
