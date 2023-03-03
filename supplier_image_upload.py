#!/usr/bin/env python3
import requests
import os
import logging

# This example shows how a file can be uploaded using
# The Python Requests module

logging.basicConfig(level=logging.DEBUG)
url = "http://localhost/upload/"
dir_name = os.path.join("supplier-data","images")
extension = ".jpeg"

def upload(file_path,dest_url):
    with open(file_path,'rb') as opened:
        r = requests.post(dest_url, files={'file':opened})

def main():
    """upload all the files in dir_name to url api"""
    
    dir_path = os.path.abspath(dir_name)
    logging.debug(dir_path)
    for name in os.listdir(dir_path):
        fullname = os.path.join(dir_path,name)
        # note - only upload the jpeg extensions
        if os.path.isfile(fullname) and os.path.splitext(name)[1] == extension :
            upload(fullname,url)
            logging.info("uploaded {} to url".format(name))

if __name__ == '__main__':
    main()
