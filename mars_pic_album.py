from mars_pic import MarsPic


class MarsPicAlbum:

    def __init__(self):
        self.my_pics = []

    def pic_count(self):
        return len(self.my_pics)

    def add_pics_from_json(self, mars_pic_json_list):
        for pic_json in mars_pic_json_list:
            self.my_pics.append(MarsPic(pic_json))

    def add_pic(self, mars_pic):
        self.my_pics.append(mars_pic)

    def find_pic_by_id(self, id_to_check):
        if type(id_to_check) is not int:
            raise ValueError("id must be an integer")
        for pic in self.my_pics:
            if pic.image_id == id_to_check:
                return pic
        return None

    def __repr__(self):
        return str(self.my_pics)

    def __str__(self):
        output_str = ""
        for pic in self.my_pics:
            output_str += str(pic) + "\n"
        return output_str

