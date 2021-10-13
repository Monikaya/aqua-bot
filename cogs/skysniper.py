import asyncio
import re
import os
import discord
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter, RequestsWebhookAdapter
import aiohttp

op = os.name == 'nt'
if op: import winsound
from concurrent.futures import ThreadPoolExecutor
from timeit import default_timer
import time

import pandas as pd
import requests

from plyer import notification

c = requests.get("https://api.hypixel.net/skyblock/auctions?page=0")
resp = c.json()
now = resp['lastUpdated']
toppage = resp['totalPages']

results = []
prices = {}

# stuff to remove
REFORGES = [" ✦", "⚚ ", " ✪", "✪", "Stiff ", "Lucky ", "Jerry's ", "Dirty ", "Fabled ", "Suspicious ", "Gilded ",
            "Warped ", "Withered ", "Bulky ", "Stellar ", "Heated ", "Ambered ", "Fruitful ", "Magnetic ", "Fleet ",
            "Mithraic ", "Auspicious ", "Refined ", "Headstrong ", "Precise ", "Spiritual ", "Moil ", "Blessed ",
            "Toil ", "Bountiful ", "Candied ", "Submerged ", "Reinforced ", "Cubic ", "Warped ", "Undead ",
            "Ridiculous ", "Necrotic ", "Spiked ", "Jaded ", "Loving ", "Perfect ", "Renowned ", "Giant ", "Empowered ",
            "Ancient ", "Sweet ", "Silky ", "Bloody ", "Shaded ", "Gentle ", "Odd ", "Fast ", "Fair ", "Epic ",
            "Sharp ", "Heroic ", "Spicy ", "Legendary ", "Deadly ", "Fine ", "Grand ", "Hasty ", "Neat ", "Rapid ",
            "Unreal ", "Awkward ", "Rich ", "Clean ", "Fierce ", "Heavy ", "Light ", "Mythic ", "Pure ", "Smart ",
            "Titanic ", "Wise ", "Bizarre ", "Itchy ", "Ominous ", "Pleasant ", "Pretty ", "Shiny ", "Simple ",
            "Strange ", "Vivid ", "Godly ", "Demonic ", "Forceful ", "Hurtful ", "Keen ", "Strong ", "Superior ",
            "Unpleasant ", "Zealous "]

# Constant for the lowest priced item you want to be shown to you; feel free to change this
LOWEST_PRICE = 999999

# Constant to turn on/off desktop notifications
NOTIFY = False

# Constant for the lowest percent difference you want to be shown to you; feel free to change this
LOWEST_PERCENT_MARGIN = 1 / 2

START_TIME = default_timer()


def fetch(session, page):
    global toppage
    base_url = "https://api.hypixel.net/skyblock/auctions?page="
    with session.get(base_url + page) as response:
        # puts response in a dict
        data = response.json()
        toppage = data['totalPages']
        if data['success']:
            toppage = data['totalPages']
            for auction in data['auctions']:
                if not auction['claimed'] and 'bin' in auction and not "Furniture" in auction[
                    "item_lore"]:  # if the auction isn't a) claimed and is b) BIN
                    # removes level if it's a pet, also
                    index = re.sub("\[[^\]]*\]", "", auction['item_name']) + auction['tier']
                    # removes reforges and other yucky characters
                    for reforge in REFORGES: index = index.replace(reforge, "")
                    # if the current item already has a price in the prices map, the price is updated
                    if index in prices:
                        if prices[index][0] > auction['starting_bid']:
                            prices[index][1] = prices[index][0]
                            prices[index][0] = auction['starting_bid']
                        elif prices[index][1] > auction['starting_bid']:
                            prices[index][1] = auction['starting_bid']
                    # otherwise, it's added to the prices map
                    else:
                        prices[index] = [auction['starting_bid'], float("inf")]

                    # if the auction fits in some parameters
                    if prices[index][1] > LOWEST_PRICE and prices[index][0] / prices[index][
                        1] < LOWEST_PERCENT_MARGIN and auction['start'] + 60000 > now:
                        results.append([auction['uuid'], auction['item_name'], auction['starting_bid'], index])
        return data


async def get_data_asynchronous():
    # puts all the page strings
    pages = [str(x) for x in range(toppage)]
    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.Session() as session:
            loop = asyncio.get_event_loop()
            START_TIME = default_timer()
            tasks = [
                loop.run_in_executor(
                    executor,
                    fetch,
                    *(session, page)  # Allows us to pass in multiple arguments to `fetch`
                )
                # runs for every page
                for page in pages if int(page) < toppage
            ]
            for response in await asyncio.gather(*tasks):
                pass


def main():
    webhook = Webhook.partial(897637962618138666,
                              "s8YfsAm1AmG0gSMA8t1dbshHlFZ1s_q5l37rKtJu_zzYb6pMSEymNzFHjReA_bIKk66b",
                              adapter=RequestsWebhookAdapter())
    # Resets variables
    global results, prices, START_TIME
    START_TIME = default_timer()
    results = []
    prices = {}

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    future = asyncio.ensure_future(get_data_asynchronous())
    loop.run_until_complete(future)

    # Makes sure all the results are still up to date
    if len(results): results = [[entry, prices[entry[3]][1]] for entry in results if (
            entry[2] > LOWEST_PRICE and prices[entry[3]][1] != float('inf') and prices[entry[3]][0] == entry[2] and
            prices[entry[3]][0] / prices[entry[3]][1] < LOWEST_PERCENT_MARGIN)]

    if len(results):  # if there's results to print

        if NOTIFY:
            notification.notify(
                title=max(results, key=lambda entry: entry[1])[0][1],
                message="Lowest BIN: " + f'{max(results, key=lambda entry: entry[1])[0][2]:,}' + "\nSecond Lowest: " + f'{max(results, key=lambda entry: entry[1])[1]:,}',
                app_icon=None,
                timeout=4,
            )

        df = pd.DataFrame(['/viewauction ' + str(max(results, key=lambda entry: entry[1])[0][0])])

        done = default_timer() - START_TIME
        for result in results:
            embed = discord.Embed(title="found stuff",
                                  description="Auction UUID: " + str(result[0][0]) + "\n Item Name: " + str(
                                      result[0][1]) + "\n Item price: {:,}".format(result[0][2]),
                                  color=discord.Colour.blurple())
            webhook.send(embed=embed, username="aqua skyblock sniper",
                         avatar_url="https://cdn.discordapp.com/attachments/875661506887426088/897269923636715541/amongie.jpg")
        webhook.send("looking for more now so stfu", username="aqua skyblock sniper",
                     avatar_url="https://cdn.discordapp.com/attachments/875661506887426088/897269923636715541/amongie.jpg")

        asyncio.run(main())



def dostuff():
    global now, toppage

    # if 60 seconds have passed since the last update
    if time.time() * 1000 > now + 60000:
        prevnow = now
        now = float('inf')
        c = requests.get("https://api.hypixel.net/skyblock/auctions?page=0").json()
        if c['lastUpdated'] != prevnow:
            now = c['lastUpdated']
            toppage = c['totalPages']
            main()
        else:
            now = prevnow
    time.sleep(0.25)


class pp(commands.Cog):

    def __init__(self, client):
        self.client = client


if True:
    main()


def setup(client):
    client.add_cog(pp(client))
