* Author:   Dries Steenberghe
* Example:  api().get_movies(), will return a list with that will be broadcasted today.

class api:

    def __init__(self):
        import datetime
        sortMovies = 0
        apiKey = '0z6a54un2dfh9bovl5v9w2b01ajccy6t'
        currentDay = datetime.datetime.today().strftime('%d-%m-%Y')
        self.apiURL = f'http://api.filmtotaal.nl/filmsoptv.xml?apikey={apiKey}&dag={currentDay}&sorteer={sortMovies}'

    def get_movies(self):
        import xmltodict
        import requests
        movies_names = []

        response = requests.get(self.apiURL)
        xmltodict = xmltodict.parse(response.content)

        for movies in xmltodict['filmsoptv']['film']:
            movie_data = []
            movie_data.append(movies['titel'])
            movie_data.append(movies['zender'])
            movie_data.append(movies['jaar'])
            movies_names.append(movie_data)

        return movies_names

