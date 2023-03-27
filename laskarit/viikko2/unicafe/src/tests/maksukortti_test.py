import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
   def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa")

    def test_lataus_oikein(self):
        self.assertNotEqual(self.Kassapaate)

    def test_ottaminen_toimii(self):
	if self.assertEqual(self.kassapaate):
		return True
	else:
		return False



