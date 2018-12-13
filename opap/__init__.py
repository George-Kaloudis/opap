name = "hbapi"

import requests, json, datetime, os
from bs4 import BeautifulSoup

url = "https://www.humblebundle.com/"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

def get_bundles():


    bundle_finder = soup.find_all("script", id="base-webpack-json-data")

    j = bundle_finder[0].text.strip()

    jstr = json.loads(j)
    jadv = jstr['navbar']['productTiles']
    bundles = {}

    for item in jadv:
        bundles[item['tile_name']] = item['url']

    return bundles


def get_items(bundle, bundle_url):

    bundle_specific_url = url + bundle_url
    tier_dict = {}
    bundle_resp = requests.get(bundle_specific_url)
    bundle_soup = BeautifulSoup(bundle_resp.text, 'html.parser')

    if bundle_url == "/monthly":

        game_finder = bundle_soup.find_all("script", id="webpack-monthly-monthly-data")

        jtext = game_finder[0].text.strip()

        jdat = json.loads(jtext)

        games = jdat['payEarlyOptions']['earlyUnlocksHumanName']
        price = jdat['navbarOptions']['priceToSubscribe']

        val = []
        val.append(bundle)
        val.append([])
        val[1].append(price)
        val[1].append(games)
    else:

        bundle_tiers = bundle_soup.select(".dd-game-row")

        for tier in bundle_tiers:
            if tier.select(".dd-header-headline"):
                tiername = tier.select(".dd-header-headline")[0].text.strip()

                product_names = tier.select(".dd-image-box-caption")
                product_names = [prodname.text.strip() for prodname in product_names]

                tier_dict[tiername] = {"products": product_names}

        val = []
        val.append(bundle)
        i = 0
        for tiername, tierinfo in tier_dict.items():
            val.append([])
            val[i+1].append(tiername.split()[1])
            val[i+1].append(", \n".join(tierinfo['products']))
            i += 1

    return val