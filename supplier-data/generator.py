#!/usr/bin/env python3

import logging 
import random
import os
import shutil

# var
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
# config for generate_description()
fruitnamefile = "fruitnames.txt"
description_text_file = "sample_text_file.txt"
descriptions_dir_path = os.path.abspath("descriptions")
no_of_files_to_generate = 20
# config for generate_img()
sample_img_path = "example.jpg"
img_dir_path = os.path.abspath("images")
no_of_images_to_generate = 20


def pull_data_from_txt(file_path):
    """pulls data from txt into a list. returns a list"""
    list = []
    with open(file_path) as file:
        for line in file:
            list.append(line.strip())
    return list

def remove_all_from_dir(dir_path):
    """removes all files from dir. use with caution. 
    currently only remove files not dir"""
    for name in os.listdir(dir_path):
        fullname = os.path.join(dir_path,name)
        if os.path.isdir(fullname):
            # item is a dir, put code here
            pass 
        else:
            # item is a file, put code here
            os.remove(fullname)

def copyfile(source, destination):
    try:
        shutil.copy(source, destination)
        logging.debug("File copied successfully.")
 
    # If source and destination are same
    except shutil.SameFileError:
        logging.error("Source and destination represents the same file.")
 
    # If there is any permission issue
    except PermissionError:
        logging.error("Permission denied.")
 
    # For other errors
    except:
        logging.error("Error occurred while copying file.")

def generate_description():
    """write a script to generate a number of txt files in this format
    <001>.txt
    <mango>
    <300> lbs
    <description text here> 
    prints ok if completed"""
    # opens fruitnamefile 
    # and add all the names into fruitnamelist
    fruitnamelist = pull_data_from_txt(fruitnamefile)
    # debug log
    for line in fruitnamelist:
        logging.debug(line)
    # opens desciption_text_file 
    # and add all the text into description_text_file
    description_text = pull_data_from_txt(description_text_file)
    # debug log
    for line in description_text:
        logging.debug(line)
    # remove all previous files in dir
    remove_all_from_dir(descriptions_dir_path)
    for index in range(no_of_files_to_generate):
        # name the file from i
        filename = "{:03}.txt".format(index)
        filepath = os.path.join(descriptions_dir_path,filename)
        # select <mango> randomly from fruitnamelist
        fruitname = random.choice(fruitnamelist)
        # select a random weight
        weight = "{} lbs".format(random.randint(1,500))
        # select a random description
        description = random.choice(description_text)
        # create file
        with open(filepath, "w") as file:
            file.write(fruitname+"\n")
            file.write(weight+"\n")
            file.write(description+"\n")
    logging.info("descriptions 000.txt to {:03}.txt generated".format(no_of_files_to_generate))

def generate_img():
    """generate x number of images in images folder
    with indexed name 000.jpeg"""
    remove_all_from_dir(img_dir_path)
    for index in range(no_of_images_to_generate):
        img_name = "{:03}.jpg".format(index)
        # copy file from example.jpg
        source = os.path.abspath(sample_img_path)
        destination = os.path.join(img_dir_path,img_name)
        copyfile(source,destination)
    logging.info("images 000.jpg to {:03}.jpg generated".format(no_of_images_to_generate))

if __name__ == '__main__':
    generate_description()
    generate_img()