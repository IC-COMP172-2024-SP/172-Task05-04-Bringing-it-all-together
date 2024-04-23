import unittest
import json
from mars_pic_album import MarsPicAlbum
import mars_data_lib


class MarsPicAlbumTest(unittest.TestCase):

    def test_mars_pic_album(self):
        my_pic_album = MarsPicAlbum()
        self.assertEqual(0, len(my_pic_album.my_pics))
        pics_json = mars_data_lib.fetch_mars_day_pics_from_file(1000)
        my_pic_album.add_pics_from_json(pics_json)
        self.assertEqual(856, len(my_pic_album.my_pics))
        self.assertEqual(102693, my_pic_album.my_pics[0].image_id)
        self.assertEqual(409065, my_pic_album.my_pics[-1].image_id)

        pics_json = mars_data_lib.fetch_mars_day_pics_from_file(4100)
        my_pic_album.add_pics_from_json(pics_json)
        self.assertEqual(1292, len(my_pic_album.my_pics))
        self.assertEqual(102693, my_pic_album.my_pics[0].image_id)
        self.assertEqual(409065, my_pic_album.my_pics[855].image_id)
        self.assertEqual(1227397, my_pic_album.my_pics[856].image_id)
        self.assertEqual(1228025, my_pic_album.my_pics[-1].image_id)

    def test_mars_pic_album_find(self):
        my_pic_album = MarsPicAlbum()
        pics_json = mars_data_lib.fetch_mars_day_pics_from_file(4100)
        my_pic_album.add_pics_from_json(pics_json)
        found_pic = my_pic_album.find_pic_by_id(1227398)
        self.assertEqual(1227398, found_pic.image_id)
        self.assertEqual("Mast Camera", found_pic.camera_name)

        with self.assertRaises(ValueError):
            my_pic_album.find_pic_by_id("1227398")
