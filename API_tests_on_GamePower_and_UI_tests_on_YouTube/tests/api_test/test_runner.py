import unittest
from concurrent.futures import ThreadPoolExecutor
from API_tests_on_GamePower_and_UI_tests_on_YouTube.infra.ui_infra.browser_wrapper import WebNavigator
from api_test import TestGamePower

test_serial_cases = [TestGamePower]
test_cases = [TestGamePower]
web_browser = WebNavigator()


def run_tests_via_one_browser(browser, test_case):
    test_case.browser = browser
    test_suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    unittest.TextTestRunner().run(test_suite)


def run_tests_for_browser_serial(browsers, serial_tests):
    for test in serial_tests:
        for browser in browsers:
            run_tests_via_one_browser(browser, test)


def run_tests_in_parallel_mode(browsers, parallel_tests):
    for test_case in parallel_tests:
        with ThreadPoolExecutor(max_workers=len(browsers)) as executor:
            for brows in browsers:
                executor.submit(run_tests_via_one_browser, brows, test_case)


if __name__ == "__main__":

    if web_browser.parallel:
        run_tests_in_parallel_mode(web_browser.get_browsers(), test_cases)

    elif web_browser.serial:
        run_tests_for_browser_serial(web_browser.get_browsers(), test_cases)
    else:
        run_tests_via_one_browser("chrome", test_serial_cases[0])
