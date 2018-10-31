# Example:  api.get_movies(), will return a list with that will be broadcasted today.
import self as self


class api:

    def __init__(self):
        import datetime

        sortMovies = 0
        apiKey = '0z6a54un2dfh9bovl5v9w2b01ajccy6t'
        currentDay = datetime.datetime.today().strftime('%d-%m-%Y')
        self.apiURL = f'http://api.filmtotaal.nl/filmsoptv.xml?apikey={apiKey}&dag={currentDay}&sorteer={sortMovies}'

    def get_title(self):
        import xmltodict
        import requests

        response = requests.get(self.apiURL)
        xmltodict = xmltodict.parse(response.content)

        movie_dict = []
        for movies in xmltodict['filmsoptv']['film']:
            title = movies['titel']
            movie_dict.append(title)

        return movie_dict

    def get_movie_data(self):
        import xmltodict
        import requests
        import csv
        import datetime

        bestand = 'film_data.csv'

        response = requests.get(self.apiURL)
        xmltodict = xmltodict.parse(response.content)

        with open(bestand, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')

            writer.writerow(('Titel', 'Synopsis', 'Starttijd'))

            for elem in xmltodict['filmsoptv']['film']:
                title = elem['titel']
                synop = elem['synopsis']
                ts = elem['starttijd']
                starttijd = datetime.datetime.utcfromtimestamp(ts).strftime('%H:%M')

                writer.writerow(title, synop, starttijd)

