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




with open('thuisbioscoop.xml', 'w', encoding= 'utf-8') as myXMLFile:
    myXMLFile.write(response.text)

XMLbioscoop = xmltodict.parse(response.text)


for i in XMLbioscoop['filmsoptv']['film']:
    xml = open("data.xml", "a")
    titel = i['titel']
    jaar = i['jaar']
    zender = i['zender']
    data = titel + jaar + zender
    print(data)
    with open("data.xml", "a") as xmlappend:
        xmlappend.write(data + "\n")

tkinter_data = open("data.xml", "r")
