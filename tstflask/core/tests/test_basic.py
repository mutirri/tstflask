
import unittest

from tstflask.core.tests.fixtures import SeleniumFixture

class BasicTest(SeleniumFixture):

    def test_title(self):

        self.driver.get(self.get_server_url())

        header = self.driver.find_element_by_css_selector('h1.handler-header')

        self.assertRegexpMatches(header.text, 'welcome')

if __name__ == '__main__':
    unittest.main()
