import requests
import json
from os.path import dirname, join


class GamerPowerAPI:

    def __init__(self):
        self.response = None
        self.url = self.read_config_data("config.json")['url']
        self.request = requests
        self.parallel = True

    # Method to get all giveaways
    def get_all_giveaways(self):
        return requests.get(self.url)

    # Method to get giveaways by platform
    def get_giveaways_by_platform(self, platform):
        return requests.get(f'{self.url}?platform={platform}').json()

    # Method to get giveaways sorted by popularity
    def get_giveaways_sorted_by_popularity(self):
        return requests.get(f'{self.url}?sort-by=popularity').json()

    # Method to get giveaways by platform, type, and sorted by date
    def get_giveaways_by_platform_type_and_sorted_by_date(self, platform, giveaway_type):
        self.response = requests.get(f'{self.url}?platform={platform}&type={giveaway_type}&sort-by=date').json()
        if 'status' in self.response:
            return 0
        else:
            return self.response

        # Method to get giveaways grouped by platform and type
    def get_giveaways_group_by_platform_and_type(self, platforms, types):
        self.response = requests.get(f'{self.url[:-9]}filter?platform={platforms}&type={types}').json()
        if 'status' in self.response:
            return 0
        else:
            return self.response

    def read_config_data(self, file):
        here = dirname(__file__)
        filename = join(here, file)
        with open(filename, 'r') as file:
            config = json.load(file)
            return config
