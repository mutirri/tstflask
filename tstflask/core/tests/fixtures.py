
import os
import unittest
import urllib2
from flask.ext.testing import LiveServerTestCase

from selenium import selenium, webdriver

from tstflask.core import make_app

class BasicFixture(LiveServerTestCase):

    def setUp(self):
        LiveServerTestCase.setUp(self)

        self.check_if_server_is_up_and_running()

    def create_app(self):
        from tstflask.core import settings

        self.settings = settings

        app = make_app()

        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = settings.PORT

        return app

    def check_if_server_is_up_and_running(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

    def tearDown(self):
        LiveServerTestCase.tearDown(self)


class SeleniumFixture(BasicFixture):

    def setUp(self):
        BasicFixture.setUp(self)

        if self.settings.HEADLESS_MODE:
            if os.environ.has_key('DISPLAY'):
                os.environ['OLD_DISPLAY'] = os.environ['DISPLAY']
            os.environ['DISPLAY'] = self.settings.HEADLESS_MODE_DISPLAY

        self.driver = webdriver.Firefox()
        self.driver.start_client()

    def tearDown(self):
        self.driver.close()

        if self.settings.HEADLESS_MODE:
            if os.environ.has_key('OLD_DISPLAY'):
                os.environ['DISPLAY'] = os.environ['OLD_DISPLAY']
            else:
                del os.environ['OLD_DISPLAY']

        BasicFixture.tearDown(self)

if __name__ == '__main__':
    unittest.main()
