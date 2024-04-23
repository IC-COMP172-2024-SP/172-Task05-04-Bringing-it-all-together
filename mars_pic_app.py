from flask import Flask, request
import mars_data_lib
import mars_pic_html_creator
from mars_pic_album import MarsPicAlbum


app = Flask(__name__)
my_album = MarsPicAlbum()


@app.route("/")
def home():
    album_html = mars_pic_html_creator.create_album_html(my_album, mars_pic_html_creator.create_pic_html)
    check_sol_form = """
            <form action="/viewsol">
                 <input type='number' name='sol'>
                 <input type='submit' value='Go to Mars day (sol)'>
            </form>
        """
    return album_html + check_sol_form


@app.route("/viewsol")
def view_sol():
    sol_str = request.args.get("sol", "")
    sol = mars_data_lib.check_and_convert_sol_str(sol_str)
    if sol != -1:
        sol_json = mars_data_lib.fetch_mars_day_pics_from_api(sol)
        temp_album = MarsPicAlbum()
        temp_album.add_pics_from_json(sol_json)
        message = mars_pic_html_creator.create_album_html(temp_album, mars_pic_html_creator.create_pic_and_add_button_html)
    else:
        message = "Invalid sol, please enter a valid sol (between 0 and 4180)"
    return message + "<br><br><a href='/'> Back to Home </a>"


@app.route("/addpic", methods=["POST"])
def add_pic_to_my_album():
    sol = int(request.form.get("sol", ""))
    camera_id = request.form.get("camera_id", "")
    image_id = int(request.form.get("image_id", ""))
    sol_json = mars_data_lib.fetch_mars_day_pics_from_api(sol, camera_id)
    temp_album = MarsPicAlbum()
    temp_album.add_pics_from_json(sol_json)
    the_pic = temp_album.find_pic_by_id(image_id)
    if the_pic is not None:
        my_album.add_pic(the_pic)
        message = f"Added new picture {id} to my album!"
    else:
        message = "pic not found, nothing added."
    return message + "<br><br><a href='/'> Back to home </a>"


if __name__ == "__main__":
    app.run(host="localhost", debug=True)