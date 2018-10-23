import datetime
import xmltodict
import requests
import pprint

pp = pprint.PrettyPrinter(indent=1)

#API Values
apiKey = '0z6a54un2dfh9bovl5v9w2b01ajccy6t'
currentDay = datetime.datetime.today().strftime('%d-%m-%Y')
sortMovies = 0
apiUrl = f'http://api.filmtotaal.nl/filmsoptv.xml?apikey={apiKey}&dag={currentDay}&sorteer={sortMovies}'
response = requests.get(apiUrl)

print(response)

with open('thuisbioscoop.xml', 'w', encoding= 'utf-8') as myXMLFile:
    myXMLFile.write(response.text)

XMLbioscoop = xmltodict.parse(response.text)

for i in XMLbioscoop['filmsoptv']['film']:
    titel = i['titel']
    jaar = i['jaar']
    zender = i['zender']

    timestamp = int(i['starttijd'])
    starttijd = datetime.datetime.utcfromtimestamp(timestamp).strftime('%H:%M:%S')

    print(titel, jaar, zender, starttijd)