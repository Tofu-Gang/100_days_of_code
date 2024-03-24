import unittest
from src.day_001_band_name_generator.band_name_generator import generate_band_name


########################################################################################################################

class TestChallenge1(unittest.TestCase):
    def test_generate_band_name(self):
        city_name = "Pilsen"
        pet_name = "Miksi"
        self.assertEqual(city_name + " " + pet_name, generate_band_name(city_name, pet_name))


########################################################################################################################

if __name__ == '__main__':
    unittest.main()

########################################################################################################################
