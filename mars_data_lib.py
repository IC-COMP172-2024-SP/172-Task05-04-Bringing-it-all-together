import requests
import json


def fetch_mars_day_pics_from_api(mars_day_num, camera_id=None):
    request_url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={mars_day_num}&api_key=DEMO_KEY"
    if camera_id is not None:
        request_url += f"&camera={camera_id}"
    print(request_url)
    response = requests.get(request_url)
    full_json = response.json()
    pics_list_json = full_json["photos"]
    return pics_list_json


def fetch_mars_day_pics_from_file(mars_day_num):
    with open(f"../data/{mars_day_num}_pics.json", "r") as mars_pic_file:
        mars_pics_json = json.load(mars_pic_file)
    pics_list_json = mars_pics_json["photos"]
    return pics_list_json


def write_test_json_to_file(mars_day_num, camera_id=None):
    rover_pics_json = fetch_mars_day_pics_from_api(mars_day_num, camera_id)
    with open(f"data/{mars_day_num}_pics.json", "w") as day_pics_file:
        json.dump(rover_pics_json, day_pics_file, indent=4)


def check_and_convert_sol_str(sol_str):
    if sol_str.isdigit():
        sol = int(sol_str)
        if 0 < sol < 4180:
            return sol
        else:
            return -1
    else:
        return -1


def main():
    # write_test_json_to_file(4110)
    write_test_json_to_file(3896, "CHEMCAM")


if __name__ == "__main__":
    main()
