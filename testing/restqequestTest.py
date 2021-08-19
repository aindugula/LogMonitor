import unittest
import sys
sys.path.append('../core/')

from service import getresponse

class TestRestRequest(unittest.TestCase):

    def test_request(self):
        dict={'machine01':'127.0.0.1', 'machine02':'127.0.0.1'}
        self.assertEqual(getresponse('http://127.0.0.1:5001/machines'), dict)

if __name__ == '__main__':
    unittest.main()                           
