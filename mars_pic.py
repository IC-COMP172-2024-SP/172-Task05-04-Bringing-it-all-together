
class MarsPic:

    def __init__(self, mars_pic_json):
        self.image_id = mars_pic_json["id"]
        self.image_url = mars_pic_json["img_src"]
        self.sol = mars_pic_json["sol"]
        self.rover_name = mars_pic_json["rover"]["name"]
        self.camera_name = mars_pic_json["camera"]["full_name"]
        self.camera_id = mars_pic_json["camera"]["name"]

    def __repr__(self):
        return f"{self.rover_name}\t{self.camera_name}\t{self.image_id}:\t{self.image_url}"



