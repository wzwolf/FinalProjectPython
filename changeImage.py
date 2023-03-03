#!/usr/bin/env python3

from PIL import Image
import os
import logging

logging.basicConfig(level=logging.DEBUG)
org_dir = os.path.join("supplier-data","images")
dest_dir = os.path.join("supplier-data","images")
format = 'JPEG' 
org_extension = '.tiff'
extension = '.jpeg'
size = (600,400)
convertmode = "RGB"

def checkdirexist(path):
    if os.path.exists(path)==False:
        logging.error("dir does not exist")
        return False
    logging.debug("{} exist".format(path))
    return True
   
def convertimage(origin, dest):
    """PIL library to update all images within ~/supplier-data/images directory to the following specifications:
    Size: Change image resolution from 3000x2000 to 600x400 pixel
    Format: Change image format from .TIFF to .JPEG"""
    try: 
        logging.debug("attempting to open {}".format(origin))
        with Image.open(origin) as im:
            im.convert(convertmode).resize(size).save(dest,format)
        checkimage(dest)
    except OSError as e:
        logging.debug(" file is not an image")

def checkimage(path):
    im = Image.open(path)
    logging.debug("=================New Size =====================")
    logging.debug(im.format)
    logging.debug(im.size)
    im.close()

def main():
    """PIL library to update all images within ~/supplier-data/images directory to the following specifications:
    Size: Change image resolution from 3000x2000 to 600x400 pixel
    Format: Change image format from .TIFF to .JPEG"""
    # check if dir exist
    org_dir_path=os.path.abspath(org_dir)
    dest_dir_path=os.path.abspath(dest_dir)
    if not checkdirexist(org_dir_path) or not checkdirexist(dest_dir_path):
        return 
    for filename in os.listdir(org_dir_path) :
        filepath = os.path.join(org_dir_path,filename)
        if os.path.isfile(filepath) and os.path.splitext(filename)[1] == org_extension:
            new_file_name = os.path.splitext(filename)[0]+extension
            filedest = os.path.join(dest_dir_path,new_file_name)
            logging.debug(filename)
            logging.debug(filepath)
            logging.debug(filedest)
            convertimage(filepath,filedest)

if __name__ == "__main__":
    main()