import unittest
import uglysoup as us

class UglyTestCase(unittest.TestCase):
    def test_rawFind(self):
        soup = us.UglySoup("toto 2 tata")
        r = soup.rawFind('toto', 'tata')
        self.assertEquals('2', r)

    def test_find(self):
        soup = us.UglySoup('<div name="toto">tata<div name="titi">tutu</div></div>')
        r = soup.find("toto", "<")
        self.assertEquals('div',r.tag)
        self.assertEquals('tata',r.s)
        self.assertEquals('toto',r.attr['name'])
        
        r = soup.find("toto", "</")
        print()
        print(r.s)
        r = r.find("titi","</")
        self.assertEquals('tutu',r.s)

    def test_findAll(self):
        soup = us.UglySoup('<div name="toto" class="test">tata<div name="titi" class="test">tutu</div></div>')
        r = soup.findAll('class="test"', "<")
        self.assertEquals(2,len(r))
        self.assertEquals('tata',r[0].s)
        self.assertEquals('tutu',r[1].s)
        self.assertEquals('toto',r[0].attr['name'])
        self.assertEquals('titi',r[1].attr['name'])

