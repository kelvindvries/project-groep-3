import xmltodict
import requests
import csv
import datetime

sortMovies = 0
apiKey = '0z6a54un2dfh9bovl5v9w2b01ajccy6t'
currentDay = datetime.datetime.today().strftime('%d-%m-%Y')
apiURL = f'http://api.filmtotaal.nl/filmsoptv.xml?apikey={apiKey}&dag={currentDay}&sorteer={sortMovies}'

response = requests.get(apiURL)
xmltodict = xmltodict.parse(response.content)
bestand = 'film_data.csv'

print(response)


def get_movie_data():
    with open(bestand, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=";")

        for elem in xmltodict['filmsoptv']['film']:
            title = elem['titel']
            synop = elem['synopsis']
            ts = elem['starttijd']
            starttijd = datetime.datetime.utcfromtimestamp(int(ts)).strftime('%H:%M')

            writer.writerow((title, synop, starttijd))




