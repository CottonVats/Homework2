import json
import requests
class CoutryInfo:
    def __init__(self, path):
        self.path = path
        with open(self.path) as contries_file:
            self.countries = json.load(contries_file)
            self.countries_iterable = self.countries.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        country_dict = self.countries_iterable.__next__()
        name = country_dict['name']['official']
        params = {
            'action':'query',
            'titles':name,
            'prop':'info',
            'inprop':'url'
        }
        link = requests.get('https://en.wikipedia.org/w/api.php', params=params)
        page_URL = link.json()['query']['pages'][0]['fullurl']
        data = {name:page_URL}
        with open(self.path, 'w') as countries_file:
            countries_file.json.dump(data)

Countries = CoutryInfo('countries.json')

