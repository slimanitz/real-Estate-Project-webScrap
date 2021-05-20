
from seLogerBot import seLogerBot
import pprint
import json


url = 'https://www.seloger.com/immobilier/locations/immo-aix-en-provence-13/bien-parking/'
url2 = 'https://www.seloger.com/immobilier/locations/immo-aix-en-provence-13/bien-parking/?LISTING-LISTpg=2'

allPosts= 'https://www.seloger.com/list.htm?projects=2&types=3&places=[{%22divisions%22:[2238]}]&surface=15/NaN&enterprise=0&qsVersion=1.0&m=search_advanced'




#bot = seLogerBot(url)
#bot.getPropertiesData()
bot = seLogerBot(allPosts)
#bot.getPropertiesData()


bot.getAllPagesPropertiesData()



