#!/usr/bin/env python3
import requests
import os
import logging

# This example shows how a file can be uploaded using
# The Python Requests module

logging.basicConfig(level=logging.DEBUG)
url = "http://localhost/upload/"
dir_name = os.path.join("supplier-data","images")

def upload(file_path,dest_url):
    with open(file_path,'rb') as opened:
        r = requests.post(dest_url, files={'file':opened})

def main():
    dir_path = ""
    logging.debug(dir_path)

if __name__ == '__main__':
    main()
