
from seLogerBot import seLogerBot
import pprint

url = 'https://www.seloger.com/immobilier/locations/immo-aix-en-provence-13/bien-parking/'
url2 = 'https://www.seloger.com/immobilier/locations/immo-aix-en-provence-13/bien-parking/?LISTING-LISTpg=2'




bot = seLogerBot(url)
bot.getPropertiesData()
bot = seLogerBot(url2)
bot.getPropertiesData()

