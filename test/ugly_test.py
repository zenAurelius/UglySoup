import unittest
import uglysoup as us

class BaseClass(unittest.TestCase):
    def test_ugly(self):
        soup = us.UglySoup("toto 2 tata")
        r = soup.rawFind('toto', 'tata')
        self.assertEquals('2', r)
