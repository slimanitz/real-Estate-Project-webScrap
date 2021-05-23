import requests
from bs4 import BeautifulSoup
import pprint
import json



headers = {
    'authority': 'www.seloger.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.seloger.com/list.htm?projects=2&types=3&places=[{%22divisions%22:[2238]}]&enterprise=0&qsVersion=1.0&m=search_advanced',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%22796fed41-956d-46f6-a51b-3bab98ca410c%22%2C%22options%22%3A%7B%22end%22%3A%222022-06-24T15%3A29%3A15.741Z%22%2C%22path%22%3A%22%2F%22%7D%7D; didomi_token=eyJ1c2VyX2lkIjoiMTc5OTlkODMtYmY4NS02ZmFmLTkzZDMtNmI5OGU3ZmY2NDRhIiwiY3JlYXRlZCI6IjIwMjEtMDUtMjNUMTU6Mjk6MzMuNjkyWiIsInVwZGF0ZWQiOiIyMDIxLTA1LTIzVDE1OjI5OjMzLjY5MloiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiZmFjZWJvb2siLCJjOm9tbml0dXJlLWFkb2JlLWFuYWx5dGljcyIsImM6bGF1bmNoZGFyLThxYThRanQ3IiwiYzpmYWNlYm9vay1idEM0Wlc2ciIsImM6aGFydmVzdC1QVlRUdFVQOCJdfSwicHVycG9zZXMiOnsiZW5hYmxlZCI6WyJhbmFseXNlZGUtVkRUVVVobjYiLCJzb2NpYWwiLCJwdXJwb3NlX2FuYWx5dGljcyIsImRldmljZV9jaGFyYWN0ZXJpc3RpY3MiLCJnZW9sb2NhdGlvbl9kYXRhIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpsYXVuY2hkYXItOHFhOFFqdDciXX0sInB1cnBvc2VzX2xpIjp7ImVuYWJsZWQiOlsiYW5hbHlzZWRlLVZEVFVVaG42Il19LCJ2ZXJzaW9uIjoyLCJhYyI6IkFrdUFDQWtzLkFrdUFDQWtzIn0=; euconsent-v2=CPGqJCpPGqJCpAHABBENBaCsAP_AAH_AAAAAH0Nf_X__b3_j-_59__t0eY1f9_7_v-0zjhfdt-8N2f_X_L8X42M7vF36pq4KuR4Eu3LBIQdlHOHcTUmw6okVrTPsbk2Mr7NKJ7PEinMbe2dYGH9_n93TuZKY7__8___z__-v_v____f_r-3_3__59X---_e_V399zLv9__3__A-UAkw1L4ALsSxwZJo0qhRAhCsJDoBQAUUAwtE1hAyuCnZXAR6ggYAITUBGBECDEFGLAIABAIAkIiAkAPBAIgCIBAACAFSAhAARsAgsALAwCAAUA0LECKAIQJCDI4KjlMCAiRaKCeysASi72NMIQyiwAoFH9FRgIlCCBYGQkLAA.f_gAD_gAAAAA; visitId=1621783773920-226657104; abtest_consent=1; _gid=GA1.2.1881666326.1621783774; _gat_UA-155862534-1=1; _gcl_au=1.1.859534463.1621783774; _hjTLDTest=1; _hjid=558463f7-34d4-46b1-8640-520c7e17f9c2; _hjFirstSeen=1; datadome=Zgq0AI8aPuzvV4IpMI.5FosIVFC5~GL1ZDRC4ZxAkIp-mL5t~LnVgbuKOiBXmEfS0S7An5e1x7Mai6cWpcbj1gSgj9f-4gcHbwxWIfx1G8; _ga_MC53H9VE57=GS1.1.1621783773.1.1.1621783779.0; _ga=GA1.2.1785679114.1621783774; _hjIncludedInSessionSample=1; _hjAbsoluteSessionInProgress=0; ry_ry-s3oa268o_realytics=eyJpZCI6InJ5XzRCQzczQjk0LUNCREYtNDYzOC1CRTE3LTU5NkQ1RjAyOThGRiIsImNpZCI6bnVsbCwiZXhwIjoxNjUzMzE5Nzc1NDgyLCJjcyI6MX0%3D; ry_ry-s3oa268o_so_realytics=eyJpZCI6InJ5XzRCQzczQjk0LUNCREYtNDYzOC1CRTE3LTU5NkQ1RjAyOThGRiIsImNpZCI6bnVsbCwib3JpZ2luIjpmYWxzZSwicmVmIjpudWxsLCJjb250IjpudWxsLCJucyI6ZmFsc2V9; realytics=1',
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
            return ""

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
                return postalCode[2].replace('(','').replace(')','')
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
        if(city ==None):
            return {
                'owner': owner,
                'price': price,
                'city': "Quartier "+departement[0],
                'departement': departement,
                'size': size,
                'url': url,
                'postalCode': postalCode
            }


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
        if response.ok:
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







