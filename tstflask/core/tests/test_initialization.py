
import unittest
import urllib2

from flask.ext.testing import LiveServerTestCase

from tstflask.core import make_app

#
# Base fixtures
#

class AFixture(unittest.TestCase):
    def setUp(self):
        print "setUp from AFixture"
    def tearDown(self):
        print "tearDown from AFixture"

class BFixture(unittest.TestCase):
    def setUp(self):
        print "setUp from BFixture"
    def create_app(self):
        app = make_app()
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        return app
    def tearDown(self):
        print "tearDown from BFixture"

class CFixture(unittest.TestCase):
    def setUp(self):
        print "setUp from CFixture"
    def tearDown(self):
        print "tearDown from CFixture"

#
# extended fixtures
#

# case 0

class My100Fixture(LiveServerTestCase, AFixture, CFixture):
    def setUp(self):
        LiveServerTestCase.setUp(self)
        AFixture.setUp(self)
        CFixture.setUp(self)
    # MUST EXISTS - LiveServerTestCase
    def create_app(self):
        app = make_app()
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        return app
    def tearDown(self):
        LiveServerTestCase.tearDown(self)
        CFixture.tearDown(self)
        AFixture.tearDown(self)

class My101Fixture(AFixture, CFixture, LiveServerTestCase):
    def setUp(self):
        AFixture.setUp(self)
        CFixture.setUp(self)
        LiveServerTestCase.setUp(self)
    # MUST EXISTS - LiveServerTestCase
    def create_app(self):
        app = make_app()
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        return app
    def tearDown(self):
        LiveServerTestCase.tearDown(self)
        CFixture.tearDown(self)
        AFixture.tearDown(self)

### case 1

class My102Fixture(BFixture, AFixture, LiveServerTestCase):
    def setUp(self):
        BFixture.setUp(self)
        AFixture.setUp(self)
        LiveServerTestCase.setUp(self)
    def tearDown(self):
        LiveServerTestCase.tearDown(self)
        AFixture.tearDown(self)
        BFixture.tearDown(self)

class My103Fixture(LiveServerTestCase, AFixture, BFixture):
    def setUp(self):
        AFixture.setUp(self)
        BFixture.setUp(self)
        LiveServerTestCase.setUp(self)
    # MUST EXISTS - LiveServerTestCase in first place of inheritance
    def create_app(self):
        app = make_app()
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        return app
    def tearDown(self):
        LiveServerTestCase.tearDown(self)
        BFixture.tearDown(self)
        AFixture.tearDown(self)

### case 2

class My104Fixture(AFixture, BFixture, LiveServerTestCase):
    def setUp(self):
        AFixture.setUp(self)
        BFixture.setUp(self)
        LiveServerTestCase.setUp(self)
    def tearDown(self):
        LiveServerTestCase.tearDown(self)
        BFixture.tearDown(self)
        AFixture.tearDown(self)

#
# tests
#

@unittest.skip('Not now')
class My100Test(My100Fixture):
    def test_server_is_up_and_running(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

@unittest.skip('Not now')
class My101Test(My101Fixture):
    def test_server_is_up_and_running(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

@unittest.skip('Not now')
class My102Test(My102Fixture):
    def test_server_is_up_and_running(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

@unittest.skip('Not now')
class My103Test(My103Fixture):
    def test_server_is_up_and_running(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

@unittest.skip('Not now')
class My104Test(My104Fixture):
    def test_server_is_up_and_running(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

#
# main
#

if __name__ == '__main__':
    unittest.main()
