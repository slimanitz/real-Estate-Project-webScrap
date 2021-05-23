
from seLogerBot import seLogerBot




allsellingPosts= 'https://www.seloger.com/list.htm?projects=2&types=3&places=[{%22countries%22:[250]}]&enterprise=0&qsVersion=1.0&m=search_advanced'
allrentingPosts= 'https://www.seloger.com/list.htm?projects=1&types=3&places=[{%22countries%22:[250]}]&geoloc=0&enterprise=0&qsVersion=1.0'



bot = seLogerBot(allsellingPosts)

bot.getAllPagesPropertiesData()










