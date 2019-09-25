import unittest
from paste.fixture import TestApp
from nose.tools import *
from lookupApp import app


class TestCode(unittest.TestCase):
    def test_url(self):
        middleware = []
        testApp = TestApp(app.wsgifunc(*middleware))
        res = testApp.get('/urlinfo/1/foobar.com:42/testurl?query')
#Are we getting an http response?
    	assert_equal(res.status, 200)
#Are we getting the expected warning message?
        res.mustcontain('DANGEROUS')   
        
if __name__ == '__main__':
    unittest.main()

