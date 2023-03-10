#! /usr/bin/env python3
import os
import requests
import logging
import re

# data format to send 
# {"name": "Test Fruit", 
# "weight": 100, # convert to int (remove lbs)
# "description": "This is the description of my test fruit", 
# "image_name": "icon.sheet.png"}

logging.basicConfig(level=logging.DEBUG)
# dest 
server_ip = ""
dest_url = 'http://{}/fruits/'.format(server_ip)
# description vars 
description_text_dir = os.path.join("supplier-data","descriptions")

def convert_data(file_path, filename):
    """takes file in filepath and return following info 
     {"name": "Test Fruit", 
     "weight": 100, # convert to int (remove lbs)
     "description": "This is the description of my test fruit", 
     "image_name": "icon.sheet.png"}
    """
    output = {}
    with open(file_path) as file:
        file.seek(0, 0)
        output["name"] = file.readline().strip()
        find_digit = re.search(r"^(\d{1,})*",file.readline().strip())
        if not (find_digit == None):
            output["weight"] = int(find_digit.groups()[0])
        else:
            logging.error("weight cannot be found in {}".format(file_path))
            return
        output["description"] = file.readline().strip() 
        output["image_name"] = os.path.splitext(filename)[0] + ".jpeg"
    return output

def main():
    """upload data from description folder and image folder"""
    # scan through description folder
    for name in os.listdir(description_text_dir):
        fullname = os.path.join(description_text_dir,name)
        logging.debug(fullname)
        if os.path.isfile(fullname) and os.path.splitext(fullname)[1] == '.txt':
            data_to_upload = convert_data(fullname,name)
            logging.debug(data_to_upload)
            response = requests.post(dest_url, data=data_to_upload)
            print(response.status_code)
            response.raise_for_status()

if __name__ == "__main__":
    main()