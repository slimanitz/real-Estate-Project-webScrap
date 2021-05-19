import requests
from bs4 import BeautifulSoup
import pprint
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'br, gzip, deflate',
    'Host': 'www.seloger.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    'Accept-Language': 'fr-fr',
    'Referer': 'https://www.seloger.com/immobilier/tout/immo-aix-en-provence-13/',
    'Connection': 'keep-alive',
}


class seLogerBot:
    url = ""
    def __init__(self,url):
        self.url = url

    def getOwner(self,soup):
        try:
            return soup.find('div', {'class': 'Contact__ContentContainer-sc-3d01ca-2 cKwmCO'}).getText().strip()
        except:
            return None

    def getPrice(self,soup):
        try:
            return soup.find('div',{'data-test':'sl.price-container'}).getText().strip()
        except:
            return None

    def getSize(self,soup):
        try:
            return soup.find('div',{'data-test':'sl.tags'}).getText().strip()
        except:
            return None

    def getCity(self,soup):
        try:
            block = soup.find('div', {'class': 'ContentZone__Address-wghbmy-1 dlWlag'})
            spans = block.findAll('span')
            return spans[1].getText().strip()

        except:
            return None

    def getDepartement(self,soup):
        try:
            block =  soup.find('div',{'class':'ContentZone__Address-wghbmy-1 dlWlag'})
            spans = block.findAll('span')
            return spans[0].getText().strip()

        except:
            return None


    def getPropertyData(self,cardSoup):
        owner = self.getOwner(cardSoup)
        price = self.getPrice(cardSoup)
        city = self.getCity(cardSoup)
        departement = self.getDepartement(cardSoup)
        size = self.getSize(cardSoup)

        return{
            'owner':owner,
            'price':price,
            'city':city,
            'Departement':departement,
            'size':size
        }


    def getPropertiesData(self):
        cardsSoup = self.getAllCards()
        for card in cardsSoup:
            pprint.pprint(self.getPropertyData(card))
            pprint.pprint("============================")



    def getAllCards(self):
        soup = self.getSoup(self.url)
        cards = soup.findAll('div', {'data-test': 'sl.card-container'})
        return cards



    def getSoup(self,url):
        response = requests.get(url,headers=headers)
        if response.ok:
            soup = BeautifulSoup(response.content,'html.parser')
            return soup





