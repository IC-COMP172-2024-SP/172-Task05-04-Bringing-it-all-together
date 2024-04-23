
def create_album_html(mars_pic_album, pic_html_creator_func):
    if mars_pic_album.pic_count() > 0:
        pic_html_strs = map(pic_html_creator_func, mars_pic_album.my_pics)
        return "<br>".join(pic_html_strs)
    else:
        return "No pictures in album yet."


def create_pic_and_add_button_html(mars_pic):
    return create_pic_html(mars_pic) + "<br>" + create_add_to_album_button(mars_pic)


def create_pic_html(mars_pic):
    start_line = f"{mars_pic.image_id}: {mars_pic.rover_name} {mars_pic.camera_name} {mars_pic.sol=}"
    image = f"<img src={mars_pic.image_url} height=200>"
    link_for_image = f"<a href={mars_pic.image_url}>{image}</a>"
    return start_line + "<br>" + link_for_image


def create_add_to_album_button(mars_pic):
    return f"""
    <form action="/addpic" method="post">
         <input type="hidden" id="image_id" name="image_id" value={mars_pic.image_id}>
         <input type="hidden" id="sol" name="sol" value={mars_pic.sol}>
         <input type="hidden" id="camera_id" name="camera_id" value={mars_pic.camera_id}>
         <input type='submit' value='Add this pic to my album'>
    </form>
    """