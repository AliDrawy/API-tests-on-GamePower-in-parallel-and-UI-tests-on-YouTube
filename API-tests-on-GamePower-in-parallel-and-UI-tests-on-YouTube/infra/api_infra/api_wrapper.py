import requests
import json
from os.path import dirname, join


class GamerPowerAPI:

    def __init__(self):
        self.response = None
        self.url = self.read_config_data("config.json")['url']
        self.request = requests
        self.parallel = True

    def api_get_request(self, url):
        self.response = self.request.get(url)
        return self.response

    def read_config_data(self, file):
        here = dirname(__file__)
        filename = join(here, file)
        with open(filename, 'r') as file:
            config = json.load(file)
            return config
