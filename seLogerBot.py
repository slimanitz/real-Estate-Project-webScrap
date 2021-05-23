import requests
from bs4 import BeautifulSoup
import pprint
import urllib.parse as urlparse
from urllib.parse import parse_qs
import datetime
import urllib.request
import json
import time





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
            return "None"

    def getPrice(self,soup):
        try:
            return int(soup.find('div',{'data-test':'sl.price-container'}).getText().strip().replace(' ','').replace('€',''))
        except:
            return 0

    def getSize(self,soup):
        try:
            return int(soup.find('ul',{'data-test':'sl.tags'}).getText().strip().split()[0])
        except:
            return 0


    def getDate(self):
        return str(datetime.date.today())


    def getCity(self,soup):
        try:
            block = soup.find('div', {'class': 'ContentZone__Address-wghbmy-1 dlWlag'})
            spans = block.findAll('span')
            return spans[1].getText().strip()

        except:
            return None

    def getRef(self,soup):
        urlsoup = soup.find('a', {'name': 'classified-link'})
        url = urlsoup['href']
        parsed = urlparse.urlparse(url)
        return parse_qs(parsed.query)['Classified-ViewId'][0]


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
                return postalCode[2].replace('(','').replace(')','')
            return postalCode[1].replace('(','').replace(')','')

        except:
            return None



    def getUrl(self,soup):
        try:
            urlsoup = soup.find('a',{'name':'classified-link'})
            url = urlsoup['href']
            return url.split('?')[0]
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
        ref = self.getRef(cardSoup)
        publishDate = self.getDate()
        if(city ==None):
            return {
                'owner': owner,
                'price': price,
                'city': "Quartier "+departement[0],
                'departement': departement,
                'size': size,
                'url': url,
                'postalCode': postalCode,
                'ref':ref,
                'publishDate':publishDate
            }


        return{
            'owner':owner,
            'price':price,
            'city':city,
            'departement':departement,
            'size':size,
            'url':url,
            'postalCode':postalCode,
            'ref':ref,
            'publishDate': publishDate
        }


    def getPropertiesData(self,url):
        cardsSoup = self.getAllCards(url)
        for card in cardsSoup:
            pprint.pprint(self.getPropertyData(card))
            pprint.pprint("============================")
            self.sendToDB(self.getPropertyData(card))




    def getAllCards(self,url):
        soup = self.getSoup(url)
        cards = soup.findAll('div', {'data-test': 'sl.card-container'})
        return cards





    def getSoup(self,url):
        response = requests.get(url,headers=headers)
        time.sleep(5)
        if response.ok:
            soup = BeautifulSoup(response.content,'html.parser')
            return soup


    def sendToDB(self,propertyData):
        myurl = "http://localhost:3000/boxs/sell"
        req = urllib.request.Request(myurl)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata = json.dumps(propertyData)
        print("////////////////////////////\n")
        print(jsondata)
        jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
        req.add_header('Content-Length', len(jsondataasbytes))
        urllib.request.urlopen(req, jsondataasbytes)

    def getAllPagesPropertiesData(self):
        soup = self.getSoup(self.url)
        pagesNumber = self.getPagesNumber(soup)
        for i in range(pagesNumber):
            newUrl = self.url+'&LISTING-LISTpg='+str(i+1)
            self.getPropertiesData(newUrl)




    def getPagesNumber(self,soup):
        pagesList = soup.find('div',{'data-test':'sl.status-container'})
        pagesNumber = pagesList.getText().strip().split(" ")[5]
        return int(int(pagesNumber)/25)







