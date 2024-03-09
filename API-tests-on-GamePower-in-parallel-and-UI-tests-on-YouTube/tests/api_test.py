import unittest
from logic.api_logic import GamerPower


class TestGamePower(unittest.TestCase):

    def setUp(self):
        self.game_power = GamerPower()
        self.response = None
        self.data = None

    # Test case to validate getting all giveaways
    def test_get_All_giveaways(self):
        self.response = self.game_power.get_all_giveaways()
        self.assertEqual(self.response.status_code, 200)

    # Test case to validate getting giveaways by platform
    def test_get_giveaways_by_platform(self):
        platform = self.game_power.choose_random_value(self.game_power.platform)
        self.data = self.game_power.get_giveaways_by_platform(platform)
        self.response = self.game_power.check_platforms_type(self.data, platform)
        self.assertTrue(self.response)

    # Test case to validate getting giveaways sorted by popularity (known bug)
    # There's a bug in this test, it's not sorted by popularity
    def test_giveaways_sorted_by_popularity(self):
        self.data = self.game_power.get_giveaways_sorted_by_popularity()
        self.response = self.game_power.check_giveaways_sorted_by_popularity(self.data)
        self.assertTrue(self.response)

    # Test case to validate receiving specific giveaway details
    def test_receiving_specific_giveaway_details(self):
        id_title_list, id_list = self.game_power.get_all_id_giveaways()
        random_id = self.game_power.choose_random_value(id_list)
        self.response = self.game_power.get_specific_giveaway_details(random_id)
        self.assertEqual(self.response['id'], random_id)
        self.assertEqual(self.response['title'], id_title_list[random_id]['title'])

    # Test case to validate getting giveaways by platform, type, and sorted by date
    def test_get_giveaways_by_platform_type_and_sorted_by_date(self):
        platform = self.game_power.choose_random_value(self.game_power.platform)
        giveaway_type = self.game_power.choose_random_value(self.game_power.type)
        self.data = self.game_power.get_giveaways_by_platform_type_and_sorted_by_date(platform, giveaway_type)
        while self.data == 0:
            platform = self.game_power.choose_random_value(self.game_power.platform)
            giveaway_type = self.game_power.choose_random_value(self.game_power.type)
            self.data = self.game_power.get_giveaways_by_platform_type_and_sorted_by_date(platform, giveaway_type)
        self.response = self.game_power.check_type_of_giveaways(giveaway_type, self.data)
        self.assertTrue(self.response)
        self.response = self.game_power.check_platforms_type(self.data, platform)
        self.assertTrue(self.response)
        self.response = self.game_power.check_giveaways_sorted_by_date(self.data)
        self.assertTrue(self.response)

    # Test case to validate getting giveaways grouped by platform and type
    def test_get_giveaways_group_by_platform_and_type(self):
        platforms_list = [self.game_power.platform[0], self.game_power.platform[2]]
        giveaway_types_list = [self.game_power.type[0], self.game_power.type[1]]
        platforms = self.game_power.return_str_for_group(platforms_list)
        giveaway_types = self.game_power.return_str_for_group(giveaway_types_list)
        self.data = self.game_power.get_giveaways_group_by_platform_and_type(platforms, giveaway_types)
        self.response = self.game_power.check_platforms_group(self.data, platforms_list, 'platform')
        self.assertTrue(self.response)
        self.response = self.game_power.check_platforms_group(self.data, giveaway_types_list, 'types')
        self.assertTrue(self.response)
