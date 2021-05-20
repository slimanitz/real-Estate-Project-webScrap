import requests
from bs4 import BeautifulSoup
import pprint
import json



headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Host': 'www.seloger.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    'Accept-Language': 'fr-fr',
    'Accept-Encoding': 'br, gzip, deflate',
    'Connection': 'keep-alive',
}


class seLogerBot:
    url = ""
    peopertyCount = 0

    def __init__(self,url):
        self.url = url

    def getOwner(self,soup):
        try:
            return soup.find('div', {'class': 'Contact__ContentContainer-sc-3d01ca-2 cKwmCO'}).getText().strip()
        except:
            return None

    def getPrice(self,soup):
        try:
            return int(soup.find('div',{'data-test':'sl.price-container'}).getText().strip().split()[0])
        except:
            return 0

    def getSize(self,soup):
        try:
            return int(soup.find('ul',{'data-test':'sl.tags'}).getText().strip().split()[0])
        except:
            return 0

    def getCity(self,soup):
        try:
            block = soup.find('div', {'class': 'ContentZone__Address-wghbmy-1 dlWlag'})
            spans = block.findAll('span')
            return spans[1].getText().strip()

        except:
            return None

    def getDepartementName(self,soup):
        try:
            block =  soup.find('div',{'class':'ContentZone__Address-wghbmy-1 dlWlag'})
            spans = block.findAll('span')
            departmentName =  spans[0].getText().strip().split()
            if len(departmentName) == 3:
                return departmentName[0]+" "+departmentName[1]
            return departmentName[0]

        except:
            return None


    def getPostalCode(self,soup):
        try:
            block =  soup.find('div',{'class':'ContentZone__Address-wghbmy-1 dlWlag'})
            spans = block.findAll('span')
            postalCode =  spans[0].getText().strip().split()
            if len(postalCode) == 3:
                return postalCode[3].replace('(','').replace(')','')
            return postalCode[1].replace('(','').replace(')','')

        except:
            return None



    def getUrl(self,soup):
        try:
            urlsoup = soup.find('a',{'name':'classified-link'})
            url = urlsoup['href']
            return url
        except:
            return None



    def getPropertyData(self,cardSoup):
        owner = self.getOwner(cardSoup)
        price = self.getPrice(cardSoup)
        city = self.getCity(cardSoup)
        departement = self.getDepartementName(cardSoup)
        size = self.getSize(cardSoup)
        url = self.getUrl(cardSoup)
        postalCode = self.getPostalCode(cardSoup)


        return{
            'owner':owner,
            'price':price,
            'city':city,
            'departement':departement,
            'size':size,
            'url':url,
            'postalCode':postalCode
        }


    def getPropertiesData(self,url):
        cardsSoup = self.getAllCards(url)
        l = []
        for card in cardsSoup:
            pprint.pprint(self.getPropertyData(card))
            pprint.pprint("============================")
            l.append(card)
        return l



    def getAllCards(self,url):
        soup = self.getSoup(url)
        cards = soup.findAll('div', {'data-test': 'sl.card-container'})
        return cards





    def getSoup(self,url):
        response = requests.get(url,headers=headers)
        print(response.content)
        if response.ok:
            print(response.content)
            soup = BeautifulSoup(response.content,'html.parser')
            return soup


    def sendToDB(self):
        for propertyData in self.getPropertiesData():
            data = json.dumps(propertyData, indent=5)
            requests.post('localhost:3000',data)

    def getAllPagesPropertiesData(self):
        soup = self.getSoup(self.url)
        pagesNumber = self.getPagesNumber(soup)
        for i in range(pagesNumber):
            newUrl = self.url+'&LISTING-LISTpg='+str(i+1)
            self.getPropertiesData(newUrl)




    def getPagesNumber(self,soup):
        pagesList = soup.find('ul',{'data-test':'sl.simplepagination-container'})
        pagesNumber = pagesList.findAll('li')
        return len(pagesNumber)-1







