from infra.api_infra.api_wrapper import GamerPowerAPI  # Importing the GamerPowerAPI class from the infra module
import random


class GamerPower(GamerPowerAPI):  # Defining a class named GamerPower that inherits from GamerPowerAPI

    def __init__(self):  # Constructor method to initialize class attributes
        super().__init__()  # Calling the constructor of the superclass (GamerPowerAPI)
        # Reading configuration data from "config.json" file and assigning to class attributes
        self.platform = GamerPowerAPI().read_config_data("config.json")['platform']
        self.type = GamerPowerAPI().read_config_data("config.json")['type']
        self.value = GamerPowerAPI().read_config_data("config.json")['value']

    # Method to get all giveaways
    def get_all_giveaways(self):
        return self.api_get_request(self.url)

    # Method to get giveaways by platform
    def get_giveaways_by_platform(self, platform):
        return self.api_get_request(f'{self.url}?platform={platform}').json()

    # Method to get giveaways sorted by popularity
    def get_giveaways_sorted_by_popularity(self):
        return self.api_get_request(f'{self.url}?sort-by=popularity').json()

    # Method to get giveaways by platform, type, and sorted by date
    def get_giveaways_by_platform_type_and_sorted_by_date(self, platform, giveaway_type):
        self.response = self.api_get_request(f'{self.url}?platform={platform}&type={giveaway_type}&sort-by=date').json()
        if 'status' in self.response:
            return 0
        else:
            return self.response

    # Method to concatenate a list of items into a string
    def return_str_for_group(self, group_list):
        group = ''
        for item in range(len(group_list)):
            group += group_list[item] + '.'
        return group[:-1]

    # Method to get giveaways grouped by platform and type
    def get_giveaways_group_by_platform_and_type(self, platforms, types):
        self.response = self.api_get_request(f'{self.url[:-9]}filter?platform={platforms}&type={types}').json()
        if 'status' in self.response:
            return 0
        else:
            return self.response

    # Method to check if a platform or giveaway type is present in the data
    def check_platforms_group(self, data, group_list, group_type):
        if group_type == 'platform':
            for platform in group_list:
                if self.check_platforms_type(data, platform):
                    return True
        else:
            for giveaway_type in group_list:
                response_boolean, for_group = self.check_type_of_giveaways(giveaway_type, data)
                if for_group:
                    return True
        return False

    # Method to get details of a specific giveaway by ID
    def get_specific_giveaway_details(self, giveaway_id):
        self.response = self.api_get_request(f'{self.url[:-1]}?id={giveaway_id}').json()
        return self.response

    # Method to choose a random value from a list
    def choose_random_value(self, list_value):
        if not list_value:
            return None
        return random.choice(list_value)

    # Method to check if a platform is present in the data
    def check_platforms_type(self, data, platform):
        for item in data:
            if platform in item['platforms']:
                return False
        return True

    # Method to check the type of giveaways in the data
    def check_type_of_giveaways(self, type, data):
        for_group_check = False
        if type == "game":
            type_to_check = "Game"
        elif type == "loot":
            type_to_check = "DLC"
        else:
            type_to_check = "Early Access"
        for item in data:
            if type_to_check != item['type']:
                return False, for_group_check
            for_group_check = True
        return True, for_group_check

    # Method to check if giveaways are sorted by popularity
    def check_giveaways_sorted_by_popularity(self, data):
        popularity = data[0]['users']
        for item in data:
            if popularity < item['users']:
                return False
            popularity = item['users']
        return True

    # Method to get IDs and titles of all giveaways
    def get_all_id_giveaways(self):
        id_and_title = {}
        id_list = []
        data = self.get_all_giveaways().json()
        for item in data:
            id_and_title[item['id']] = {"title": item['title']}
            id_list.append(item['id'])
        return id_and_title, id_list

    # Method to check if giveaways are sorted by date
    def check_giveaways_sorted_by_date(self, data):
        dates = []
        for item in data:
            dates.append(int(''.join(char for char in item['published_date'] if char.isdigit())))
        bigger_date = dates[0]
        for date in dates:
            if date > bigger_date:
                return False
            bigger_date = date
        return True
