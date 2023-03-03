#!/usr/bin/env python3

import os
import datetime
import reports
import logging
import re

logging.basicConfig(level=logging.DEBUG)
description_text_dir = os.path.join("supplier-data","descriptions")

def content_from_dir():
    """ report_input - dictionary of values
    takes processed data from supplier-data/description
    return 
    Processed Update on <Today's date>
    [blank line]
    name: <Apple>
    weight: <500> lbs
    [blank line]
    name: <Avocado>
    weight: <200> lbs
    [blank line]
    ...
    """
    content = ""
    for name in os.listdir(description_text_dir):
        fullname = os.path.join(description_text_dir,name)
        logging.debug(fullname)
        if os.path.isfile(fullname) and os.path.splitext(fullname)[1] == '.txt':
            data = convert_data(fullname,name)
            logging.debug(data)
            if data != None:
                content += data
    return content

def convert_data(file_path, filename):
    """takes file in filepath and return the following
    name: Apple
    <br/>
    weight: 500 lbs
    <br/>
    <br/>
    """
    with open(file_path) as file:
        file.seek(0, 0)
        name = file.readline().strip()
        weight = file.readline().strip()
    return "name: {} <br/> weight: {} <br/><br/>".format(name,weight)

def main():
    """  """
    # generate pdf 
    attachment = "/tmp/processed.pdf"
    title = "Processed Update on " + datetime.date.today().strftime("%d/%m/%Y")
    paragraph = content_from_dir() 
    reports.generate_report(attachment, title, paragraph)
    # generate email







if __name__ == "__main__":
    main()
    pass
