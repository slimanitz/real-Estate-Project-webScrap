
from seLogerBot import seLogerBot





allsellingPosts= 'https://www.seloger.com/list.htm?projects=2&types=3&places=[{%22countries%22:[250]}]&enterprise=0&qsVersion=1.0&m=search_advanced'
allrentingPosts= 'https://www.seloger.com/list.htm?projects=1&types=3&places=[{%22countries%22:[250]}]&sort=d_dt_crea&enterprise=0&qsVersion=1.0&m=search_refine'



bot = seLogerBot(allrentingPosts,"rent")
bot.getAllPagesPropertiesData()

bot = seLogerBot(allsellingPosts,"sell")
bot.getAllPagesPropertiesData()



















