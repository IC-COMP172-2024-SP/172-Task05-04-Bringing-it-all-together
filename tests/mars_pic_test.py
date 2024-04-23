import unittest
import json
from mars_pic import MarsPic


class MarsPicTest(unittest.TestCase):

    def test_mars_pic(self):
        with open("../data/1000_pics.json", "r") as mars_pic_file:
            mars_pics_json = json.load(mars_pic_file)
        my_pic = MarsPic(mars_pics_json["photos"][0])
        self.assertEqual(102693, my_pic.image_id)
        self.assertEqual("Curiosity", my_pic.rover_name)
