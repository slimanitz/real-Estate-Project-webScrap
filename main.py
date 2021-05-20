import datetime

from seLogerBot import seLogerBot
import pprint
import json


url = 'https://www.seloger.com/immobilier/locations/immo-aix-en-provence-13/bien-parking/'
url2 = 'https://www.seloger.com/immobilier/locations/immo-aix-en-provence-13/bien-parking/?LISTING-LISTpg=2'

allsellingPosts= 'https://www.seloger.com/list.htm?projects=2&types=3&places=[{%22divisions%22:[2238]}]&enterprise=0&qsVersion=1.0&m=search_advanced'
allrentingPosts= 'https://www.seloger.com/list.htm?projects=1&types=3&places=[{%22countries%22:[250]}]&geoloc=0&enterprise=0&qsVersion=1.0'





#bot = seLogerBot(url)
#bot.getPropertiesData()
bot = seLogerBot(allsellingPosts)
#bot.getPropertiesData()

bot.getAllPagesPropertiesData()




