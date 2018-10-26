# Author:   Dries Steenberghe
# Example:  api.get_movies(), will return a list with that will be broadcasted today.


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

        api_data = open("api_data.xml", "w")
        api_data.write("")
        movies_names = []

        response = requests.get(self.apiURL)
        xmltodict = xmltodict.parse(response.content)



        for movies in xmltodict['filmsoptv']['film']:

            title = movies['titel']
            channel = movies['zender']
            year = movies['jaar']
            r_string = title + " " + year + " " + channel + "\n"
            api_data.write(r_string)

        api_data.close()
        return open("api_data.xml", "r").read()




print(api().get_movies())